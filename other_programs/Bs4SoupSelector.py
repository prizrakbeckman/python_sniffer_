import os, requests, bs4


def selectElements(file):
    if not file.endswith('.html'):
        while true:
            print('Please enter a valid path for an html file')
            file = input()
            if file.endswith('.html'):
                break;
    exampleFile = open(file)
    exampleSoup = bs4.BeautifulSoup(exampleFile,features="html.parser")
    type(exampleSoup)
    print(exampleSoup.select('#author'))
    print(exampleSoup.select('input[type="submit"]'))
    pElems = exampleSoup.select('p')
    print(str(pElems[0]))
    print(pElems[0].getText())
    print(pElems[0].get('id'))
    
os.chdir('C:\\Users\\HP\\Desktop\\latestDir')
print('Enter the html to parse')
file = input()
selectElements(file)
