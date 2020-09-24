import os, PyPDF2

def usePdfFile(file):
    pdfFileObj = open(file,'rb')
    textExtracted = open('fileTextExtracted.txt','w', encoding='utf-8')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPage = pdfReader.numPages
    print(numPage)
    for i in range(numPage):
        s = pdfReader.getPage(i).extractText()
        textExtracted.write(s)
        print('Page '+ str(i+1)+' written')

def createNewPdfFile(file):
    
    #Merge two pages in one
    #minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

    i = 0
    newName= file +'-'+ str(i)+'.pdf'
    while os.path.exists(newName):
        i = i+1
        newName= file +'-'+ str(i)+'.pdf'
    print('All good')
    pdf1File = open(file,'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdfWriter = PyPDF2.PdfFileWriter()

    #Instruction in comment to encrypt a file
    #pdfWriter.encrypt('swordzbi')

    
    for j in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(j)
        pdfWriter.addPage(pageObj)
    pdfOutputtedFile = open(newName,'wb')
    pdfWriter.write(pdfOutputtedFile)
    pdfOutputtedFile.close()
    pdf1File.close()
    
os.chdir('C:\\Users\\HP\\Desktop\\titiza')
#usePdfFile('grayhathacking.pdf')
createNewPdfFile('grayhathacking.pdf')
