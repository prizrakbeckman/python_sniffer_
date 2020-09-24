import os, shelve, pyperclip, sys

os.chdir('C:\\Users\\HP\\Desktop\\titiza')
mcbShelf = shelve.open('mcb')
#pyperclip.copy()
#s = pyperclip.paste()
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(mcbShelf[sys.argv[2]])
elif len(sys.argv)==2:
    if sys.argv[1].lower() == 'list':
        print('list operation')
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('listing')
        print('******** '+pyperclip.paste()+' ********')
    elif sys.argv[1] in mcbShelf:
        print('load operation')
        pyperclip.copy(str(mcbShelf[sys.argv[1]]))
        print('******** '+pyperclip.paste()+' ********')
print('closing the file')
mcbShelf.close()
