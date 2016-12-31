import PyPDF2

pdf1 = open('/home/zekelabs/Downloads/awa.pdf','rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1)

print pdf1Reader.getPage(0).extractText()

pdfwr = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
     pageObj = pdf1Reader.getPage(pageNum)
     pdfwr.addPage(pageObj)


pdfout = open('out.pdf','wb')
pdfwr.write(pdfout)
pdfout.close()
