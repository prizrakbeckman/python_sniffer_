import smtplib,getpass

def sendmail(host,port,mail,password,receiver,mailBody):
    print('Getting started')
    smtpObj = smtplib.SMTP(host,port)
    print('Getting Step 1')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail,password)
    smtpObj.sendmail(mail,receiver,mailBody)
    print('mail sent ')
    smtpObj.quit()

print('Enter host')
host = input()
print('Enter port')
port = int(input())
print('Enter mail')
mail = input()
print('Enter password')
password = getpass.getpass('Password:')
print('Enter receiver')
receiver = input()
print('Enter MailBody')
mailBody = input()

sendmail(host,port,mail,password,receiver,mailBody)
