import requests, bs4, os

def createBeautifulSoupObj(url):
    res = requests.get(url)
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text)
    type(noStarchSoup)
    print(str(noStarchSoup))

def openHtmlFile(file):
    exampleFile = open(file)
    exampleSoup = bs4.BeautifulSoup(exampleFile)
    type(exampleSoup)
    print(str(exampleSoup))


os.chdir('C:\\Users\\HP\\Desktop\\latestDir')
print('Please choose to parse a File or Url')
choice = int(input())
if choice == 1:
    print('you chose Url')
    url = input()
    createBeautifulSoupObj(url)
else:
    print('you chose to parse a file')
    file = input()
    openHtmlFile(file)
