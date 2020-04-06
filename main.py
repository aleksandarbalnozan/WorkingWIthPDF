import PyPDF2


reader = PyPDF2.PdfFileReader(open('algoanddata.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    output.addPage(page)

with open('new pdf.pdf', 'wb') as file:
    output.write(file)
