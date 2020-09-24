import os, openpyxl, smtplib, sys, time

def useFile(file):
    listEmails = {}
    if os.path.exists(file):
        wb = openpyxl.load_workbook(file)
        sheet = wb.get_sheet_by_name('Feuil1')
        #print(sheets)
        i = sheet.max_row
        j = sheet.max_column
        #lastCol = sheet.get_highest_column()
        print(str(j))
        
        for k in range(1,i):
            val = str((sheet.cell(row=k,column=j-1).value))
            print(val)
            listEmails[val]=(sheet.cell(row=k,column=j).value)
        print(listEmails)
    return listEmails
def connect(email,password, listEmails):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email,password)
    for name,email in listEmails.items():
        print("email : "+email)
        body = "Subject: %s dues unpaid.\nDear %s,\nRecords show that you have not"
        "paid dues for %s. Please make this payment as soon as possible. Thank you!"
        
        print('sending email to '+email)
        time.sleep(2)
        sendmailStatus = smtpObj.sendmail('my_email_address@gmail.com', email, body)

os.chdir('C:\\Users\\HP\\Desktop\\titiza')
listEMails1 = useFile('emails.xlsx')
print("List ")
val = useFile('emails.xlsx')
print(val)
connect('adamlinguardpr@gmail.com','TR4CK!|\|G',val)
