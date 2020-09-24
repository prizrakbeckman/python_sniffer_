import bs4, webbrowser, os, requests, sys, time, pyperclip

print('Googling ...')
time.sleep(2)
print('Googling again...')
if len(sys.argv)>1:
    print('Argument found '+str(sys.argv))
    res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
   #webbrowser.open('http://google.com/search?q='+' '.join(sys.argv[1:]))
else:
    print('Argument not found '+pyperclip.paste())
    res = requests.get('http://google.com/search?q='+' '.join(pyperclip.paste()))    
   #webbrowser.open('http://google.com/search?q='+pyperclip.paste())
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linksElems = soup.select('.r a')
#print(res)
numOpen = min(2, len(linksElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linksElems[i].get('href'))
