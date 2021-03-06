# MERGING TWO PDFs

from PyPDF2 import PdfFileReader, PdfFileWriter

write_obj=PdfFileWriter()
pdf_list = ["/home/hidayat7z/PDFS/pdfone.pdf", "/home/hidayat7z/PDFS/pdftwo.pdf"]

for i in pdf_list:

    read_obj = PdfFileReader(i)         #pdf file is stored as object
    pages = read_obj.getNumPages()      #number of pages in the pdf file is stored in 'pages'
    
    for j in range(pages):              #adding each page of the pdf to the read_obj
		  p=read_obj.getPage(j)             #each page gets stored in p
		  write_obj.addPage(p)              #each page gets added to write_obj

pdf_file=open("/home/hidayat7z/PDFS/FINALpdf.pdf",'wb')                #creating a file with desired name
write_obj.write(pdf_file)                                              #creating a pdf file from the write_obj

                              #The wb indicates that the file is opened for writing in binary mode. 
                              #When writing in binary mode, Python makes no changes to data as it is written to the file.
