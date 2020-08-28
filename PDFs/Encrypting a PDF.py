# ENCRYPTING A PDF

from PyPDF2 import PdfFileReader, PdfFileWriter

write_obj=PdfFileWriter()
pdf_list = ["/home/hidayat7z/PDFS/pdfone.pdf", "/home/hidayat7z/PDFS/pdftwo.pdf"]

for i in pdf_list:

    read_obj = PdfFileReader(i)
    pages = read_obj.getNumPages()      
    
    for j in range(pages):              
		p=read_obj.getPage(j)               
		write_obj.addPage(p)                

#MAIN PART:     

write_obj.encrypt('hidayatother','hidayatmine',True)

pdf_file=open("/home/hidayat7z/PDFS/FINALpdf.pdf",'wb')
write_obj.write(pdf_file)




########## ANOTHER METHOD: (in general)

from pyPDF2 import PdfFileReader, PdfFileWriter

with open("input.pdf", "rb") as in_file:
    input_pdf = PdfFileReader(in_file)

output_pdf = PdfFileWriter()
output_pdf.appendPagesFromReader(input_pdf)         #copying from input to output
output_pdf.encrypt("password")

with open("output.pdf", "wb") as out_file:
        output_pdf.write(out_file)
