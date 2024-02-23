# Read the TSV file
with open('../data/table/annotation_key.txt', 'r') as file:
    lines = file.readlines()

html_table = '<table id="impact">\n<thead>\n<tr>\n'
headers = lines[0].strip().split('\t')
for header in headers:
    html_table += f'<th>{header}</th>\n'
html_table += '</tr>\n</thead>\n<tbody>\n'

for line in lines[1:]:
    cells = line.strip().split('\t')
    html_table += '<tr>\n'
    for cell in cells:
        html_table += f'<td>{cell}</td>\n'
    html_table += '</tr>\n'

html_table += '</tbody>\n</table>>'

# Write the HTML table to a file
with open('../data/table/annotation_key_table.html', 'w') as file:
    file.write(html_table)
