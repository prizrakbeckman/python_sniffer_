import os,requests


def downloadStuff(url):
    try:
        i = 0
        res = requests.get(url)
        res.raise_for_status()
        while true:
            print('File exists ')
            if os.path.exists('RomeoAndJuliet'+str(i)+'.txt'):
                i = i+1
            else:
                print('New file created')
                playFile = open('RomeoAndJuliet'+str(i)+'.txt','wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()
    except Exception as exc:
        print('Error was in %s' % (exc))

os.chdir('C:\\Users\\HP\\Desktop\\latestDir')
url = input()
downloadStuff(url)
