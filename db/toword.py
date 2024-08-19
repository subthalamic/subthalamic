import pandas as pd
from docx import Document
from docx.shared import Inches

# Read CSV file into a DataFrame
csv_file = 'registre/22.csv'
df = pd.read_csv(csv_file)

# Create a new Word document
doc = Document()

# Add a title or any text
doc.add_heading('Registru Probe', level=1)
doc.add_paragraph('This document contains the data from the CSV file and some additional text.')

# Add a table to the Word document
table = doc.add_table(rows=1, cols=len(df.columns))
table.style = 'Table Grid'

# Add the header row
hdr_cells = table.rows[0].cells
for i, column_name in enumerate(df.columns):
    hdr_cells[i].text = column_name

# Add the rest of the data
for index, row in df.iterrows():
    row_cells = table.add_row().cells
    for i, cell in enumerate(row):
        row_cells[i].text = str(cell)

# Add some more text if needed
doc.add_paragraph('This is some additional text added after the table.')

# Save the document
doc_file = 'rapoarte.docx'
doc.save(doc_file)

print(f"Document saved as {doc_file}")
