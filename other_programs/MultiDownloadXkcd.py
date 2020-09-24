import requests, os, bs4, threading
os.makedirs('xkcd',exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' %(urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup= bs4.BeautifulSoup(res.text)
        #Find Url of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

        #Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

os.chdir('C:\\Users\\HP\\Desktop\\newFolder')
 # Create and start the Thread objects.
downloadThreads = []
for i in range(0,1400,100):
    downloadThread = threading.Thread(target=downloadXkcd(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
for downloadThread_ in downloadThreads:
    downloadThread_.join()
print('Done.')
