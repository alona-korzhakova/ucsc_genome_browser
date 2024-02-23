##########################################################################################
# Note! currently, you should have access to UCSD Expanse system for this script to work #
##########################################################################################

import os
import re
import csv

def extract_number_and_tf(track_file):
    pattern = re.compile(r'IMPACT_(\d+)_predictions_(\w+)\.bw')

    match = re.match(pattern, track_file)

    if match:
        number = match.group(1)
        tf = match.group(2)
        return f"{number}_{tf}"

    return None

def get_id_from_csv(csv_file, track_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == os.path.splitext(track_file)[0]:
                return row[1]
    return None

def get_color(color_index):
    colors = [
        "255,188,66",
        "216,17,89",
        "143,45,86",
        "33,131,128",
        "115,210,222"
    ]
    return colors[color_index % len(colors)]

hub_file = '../data/conf/hub.txt'
base_dir = '/expanse/lustre/projects/ddp412/akorzhakova/IMPACT/bedgraphs/predictions_bw' # TODO: upload all the bigWig files as a single archive to the web, preserving the entire hierarchy
galaxy_ids_dir = '../data/table/galaxy_track_ids/'
color_index = 0
visible_tissue = "BLOOD"
visible_cells = {"b_cell", "cd4_t_cell", "dendritic_cell", "lymphoblastoid", "macrophage", "monocyte", "t_cell", "th1", "th2", "treg"}

with open(hub_file, 'w') as hub_file:

    # static section
    hub_file.write("hub ImpactHub\n")
    hub_file.write("shortLabel IMPACT regulatory element activity\n")
    hub_file.write("longLabel Cell-type-specific regulatory element activity profiles across 707 unique "
                    "combinations of transcription factor-cell type pairs. IMPACT predicts the epigenetic "
                    "regulatory activity related to a particular transcription factor in a given cell type. "
                    "IMPACT scores are probabilistic, ranging from 0 to 1.\n")
    hub_file.write("useOneFile on\n")
    hub_file.write("email korzhakova.alyona@gmail.com\n")
    hub_file.write("descriptionUrl https://www.amariutalab.org/genomebrowser\n")
    hub_file.write("\n")
    hub_file.write("genome hg19\n")
    hub_file.write("\n")

    for tissue in sorted(os.listdir(base_dir)):
        tissue_path = os.path.join(base_dir, tissue)

        if os.path.isdir(tissue_path):
            tissue_pascal_case = tissue.capitalize()

            # tissue super track
            hub_file.write(f"track superTrack{tissue_pascal_case}\n")
            if tissue == visible_tissue:
                hub_file.write( "superTrack on show\n")
            else:
                hub_file.write( "superTrack on\n")
            hub_file.write(f"shortLabel {tissue.upper()}\n")
            hub_file.write(f"longLabel {tissue_pascal_case} Tissue\n")
            hub_file.write( "html https://genome.ucsc.edu/goldenPath/help/examples/hubExamples/templatePage.html\n")
            hub_file.write( "\n")

            csv_file = os.path.join(galaxy_ids_dir, f"{tissue.lower()}.csv")

            for cell in sorted(os.listdir(tissue_path)):
                cell_path = os.path.join(tissue_path, cell)

                if os.path.isdir(cell_path):
                    cell_pascal_case = ''.join(word.capitalize() for word in cell.split('_'))
                    cell_with_whitespaces = cell.replace('_', ' ')
                    multiwig_name = f"{tissue_pascal_case}{cell_pascal_case}MultiWig"

                    # cell type multi wig
                    hub_file.write(f"    track {multiwig_name}\n")
                    hub_file.write(f"    parent superTrack{tissue_pascal_case}\n")
                    hub_file.write( "    container multiWig\n")
                    hub_file.write(f"    shortLabel {tissue.lower()} {cell_with_whitespaces}\n")
                    hub_file.write(f"    longLabel {tissue.upper()}: {cell_with_whitespaces}\n")
                    hub_file.write( "    type bigWig\n")
                    if tissue == visible_tissue and cell not in visible_cells:
                        hub_file.write( "    visibility hide\n")
                    else:
                        hub_file.write( "    visibility full\n")
                    hub_file.write( "    aggregate transparentOverlay\n")
                    hub_file.write( "    showSubtrackColorOnUi on\n")
                    hub_file.write( "    maxHeightPixels 500:50:8\n")
                    hub_file.write( "    viewLimits 0:1\n")
                    hub_file.write( "\n")

                    color = get_color(color_index)
                    color_index += 1

                    for track_file in sorted(os.listdir(cell_path)):
                        track_file_path = os.path.join(cell_path, track_file)

                        if os.path.isfile(track_file_path):
                            number_and_tf = extract_number_and_tf(track_file)
                            id_from_csv = get_id_from_csv(csv_file, track_file)

                            # Construct bigDataUrl
                            if id_from_csv:
                                big_data_url = f"https://usegalaxy.org/api/datasets/{id_from_csv}/display?to_ext=bigwig"

                                # cell track
                                hub_file.write(f"        track {number_and_tf}\n")
                                hub_file.write(f"        bigDataUrl {big_data_url}\n")
                                hub_file.write(f"        shortLabel {number_and_tf}\n")
                                hub_file.write(f"        longLabel {tissue.upper()}: {cell_with_whitespaces}\n")
                                hub_file.write(f"        parent {multiwig_name}\n")
                                hub_file.write( "        type bigWig\n")
                                hub_file.write( "        visibility full\n")
                                hub_file.write(f"        color {color}\n")
                                hub_file.write( "\n")
