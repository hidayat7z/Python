# ADDING WATERMARK to a PDF

from PyPDF2 import PdfFileReader, PdfFileWriter

pdf= PdfFileReader("/home/hidayat7z/PDFS/pdfone.pdf")
watermark=PdfFileReader("/home/hidayat7z/PDFS/watermark.pdf")

#we need to add watermark to each page

page_w=watermark.getPage(0)     #watermark is stored in page_ object

new_pdf=PdfFileWriter()         #new pdf file object
pages=pdf.getNumPages() 

for i in range(pages):
    
	page=pdf.getPage(i)        #each page of the pdf gets stored in 'page' object
	page.mergePage(page_w)     #merge this page with page_w object
	new_pdf.addPage(page)      #new page thus obtained is added to the new pdf file object
    
pdf_file=open("/home/hidayat7z/PDFS/RESULTANT.pdf",'wb')
new_pdf.write(pdf_file)

pdf_file.close()
