import PyPDF2

# create objects of pdf-s
templete = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(templete.getNumPages()):
    # go thro all pages in templete
    page = templete.getPage(i)
    # merge two pages
    page.mergePage(watermark.getPage(0))
    # add page in memory so it can be saved later
    output.addPage(page)
    print(f'page {i} done')

with open('new_water_pdf.pdf', 'wb') as file:
    # save file form memory
    output.write(file)
print('All done!')
