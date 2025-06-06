import sys
from datetime import datetime
from PyPDF2 import PdfReader
from docx import Document

documento_pdf = sys.argv[1]
documento_word = Document()

reader = PdfReader(documento_pdf)
text = ""

for page in reader.pages:
    text += page.extract_text()

documento_word.add_paragraph(text)
name = str(datetime.now())
documento_word.save(f'/home/ruben/Documentos/{name}.docx')
