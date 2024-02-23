# IMPACT Track Hub on the UCSC Genome Browser

> IMPACT represents cell-type-specific regulatory element activity profiles across 707 unique combinations of transcription factor-cell type pairs. The IMPACT model predicts the epigenetic regulatory activity related to a particular transcription factor in a given cell type. IMPACT scores are probabilistic, ranging from 0 to 1.
<br>

![IMPACT Track Hub](https://raw.githubusercontent.com/alona-korzhakova/ucsc_genome_browser/master/data/image/IMPACT_on_genome_browser.png)

*A snapshot of IMPACT visualization on the UCSC Genome Browser. This image represents a small part of the comprehensive data available in our track hub.*

### Description

This is a hosting repository for IMPACT tracks on the UCSC Genome Browser. It includes essential configuration files and software necessary for maintaining the hub on the genome browser. The *data* directory contains configuration files for the IMPACT hub, as well as some additional data used for the automatic generation of these files. The *scripts* directory houses the automation itself.

### Data Access

The core data, comprising IMPACT predictions, is stored on Galaxy and can be accessed by visiting the [Published Histories](https://usegalaxy.org/histories/list_published) page on Galaxy and searching for **user_eq:impact_predictions**.

### Genome Browser

To access the IMPACT Track Hub, go to [HubConnect](https://genome.ucsc.edu/cgi-bin/hgHubConnect) page of the UCSC Genome Browser, navigate to the **Public Hubs** tab, and connect **IMPACT regulatory element activity** from the available list.<br>
If for any reason this doesn't work - you can access the hub directly by following the [link](http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&hubUrl=https://raw.githubusercontent.com/alona-korzhakova/ucsc_genome_browser/master/data/conf/hub.txt).

For a detailed project description, please visit our IMPACT hub on the UCSC Genome Browser.

### Acknowledgments

IMPACT modeling by Tiffany Amariuta, PI Amariuta Lab, University of California, San Diego in the Halıcıoğlu Data Science Institute and the Division of Biomedical Informatics.<br>
IMPACT predictions and UCSC Track visualization by Alona Korzhakova, Computational Data Science Researcher in the Amariuta Lab.
