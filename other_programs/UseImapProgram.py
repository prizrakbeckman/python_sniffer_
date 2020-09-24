import imapclient,pyzmail,pprint

def useImap(email,password,imapPort):
    imapObj = imapclient.IMAPClient(imapPort, ssl=True)
    imapObj.login(email,password)
    print('Searching through inbox')
    imapObj.select_folder('INBOX', readonly=True)
    UIDs = imapObj.search(['SINCE 05-Oct-2018'])
    rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
    message = pyzmail36.PyzMessage.factory(rawMessages[40041]['BODY[]'])
    print(str(message))
    print(message.get_addresses('from'))
    print(message.get_addresses('to'))
    print(message.get_addresses('cc'))
    print(message.get_addresses('bcc'))
    print(message.text_part != None)
    print(message.text_part.get_payload().decode(message.text_part.charset))
    imapObj.logout()

def listFoldersImap(email,password,imapPort):
    imapObj = imapclient.IMAPClient(imapPort, ssl=True)
    imapObj.login(email,password)
    print('listing folder inbox')
    pprint.pprint(imapObj.list_folders())
    imapObj.logout()
    print('Logging out')

imapPort = 'imap.gmail.com'
email = ''
password = ''
#useImap(email,password,imapPort)
listFoldersImap(email,password,imapPort)
