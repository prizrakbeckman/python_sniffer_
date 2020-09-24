import requests, os, bs4


def downloadXkcd(url,path):
    i = 0
    while not url.endswith('#') and i < 3:
        print('Download page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        i+=1
    print('Done.')        
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = 'http:'+comicElem[0].get('src')
        print(comicUrl+'*********')
        print('Download image %s...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    print(path)
    imageFile = open(path+'\\zabi.png','wb')
    for chunk in res.iter_content(10000):
        imageFile.write(chunk)
    imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url ='http://xkcd.com'+prevLink.get('href')
    print(url)
    
url = 'http://xkcd.com'
os.chdir('C:\\Users\\HP\\Desktop\\titiza')
os.makedirs('xkcd',exist_ok=True)
os.chdir('xkcd')
path = os.getcwd()
downloadXkcd(url,path)
