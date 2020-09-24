import os, requests

def getHttpContent(s):
    
    try:
        codeVal = 0
        res = requests.get(s)
        #res.status_code == requests.codes.ok:
        print('Content found')
        fileN = open('fileResponse.txt','w',encoding='utf-8')
        fileN.write(str(res.text))
        print(res.text[:250])
        codeVal = 200
        
        return codeVal
    except Exception as exc:
        print('the problem was in %s ' %(exc))
    

os.chdir('C:\\Users\\HP\\Desktop\\titiza\\test')

s = input()
print(getHttpContent(s))
