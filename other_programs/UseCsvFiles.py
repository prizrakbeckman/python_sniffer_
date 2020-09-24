import os,csv

def useCsvFile(file):
    exampleFile = open(file)
    exampleReader = csv.reader(exampleFile)
    #exampleData = list(exampleReader)
    #print(exampleData)
    
   # Show element by element
   # for elemList in exampleData:
   #     for elem in elemList:
   #         print('***********'+elem+'*********')

    for row in exampleReader:
        print('Line number '+str(exampleReader.line_num)+' '+str(row))

def writeCsv(fileOutput, fileInput):
    fileOutput = open(fileOutput,'w',newline='')
    outputWriter = csv.writer(fileOutput)
    fileInput = open(fileInput)
    inputReader = csv.reader(fileInput)
    outputWriter.writerow(['Zabi','Twil','Zbibz'])
    for row in inputReader:
        if inputReader.line_num == 1:
            print('Zabii')
            continue
        outputWriter.writerow(row)
    outputWriter.writerow(['Fin','Fin','Fin'])
    fileOutput.close()
    print('File written successfully')


os.chdir('C:\\Users\\HP\\Desktop\\titiza')
#useCsvFile('test.csv')
writeCsv('fileOuputted11.csv','test.csv')
