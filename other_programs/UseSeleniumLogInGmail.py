import time
from selenium import webdriver

#Login automatically using selenium
def loginIntoGmail(url):
    browser = webdriver.Firefox(executable_path=r'C:/Users/HP/AppData/Local/Programs/Python/Python36/BrowersDriver/geckodriver.exe')
    browser.get(url)

    #Enter login
    loginElem = browser.find_element_by_id('identifierId')
    print('login in '+url)
    loginElem.send_keys('adam.hardoumi')
    print('login entered')
    suivButt = browser.find_element_by_class_name('CwaK9')
    suivButt.click()
    time.sleep(2)

    #Enter password
    pwElem = browser.find_element_by_class_name('whsOnd')
    pwElem.send_keys('')
    print('pw entered')
    
    #input ENTER key
    pwElem.send_keys(u'\ue007')
    print('Submited ?')
    time.sleep(15)

    #Compose Email button
    composeButton = browser.find_element_by_class_name('z0')
    composeButton.click()
    time.sleep(5)

    #Fill email values
    receiverEmail = browser.find_element_by_xpath('//textarea[1]')
    print(type(receiverEmail))
    receiverEmail.send_keys('')

    #Fill subject subject & content mail
    subjectVal= browser.find_element_by_id(':ph')
    subjectVal.send_keys('test to be sent')
    contentVal = browser.find_element_by_id(':qm')
    contentVal.send_keys('Test test tes')

def composeEmail(url):
    browser = webdriver.Firefox(executable_path=r'C:/Users/HP/AppData/Local/Programs/Python/Python36/BrowersDriver/geckodriver.exe')
    browser.get(url)
    composeButton = browser.find_element_by_class_name('z0')
    composeButton.click()
    
loginIntoGmail('http://gmail.com')
#composeEmail('https://mail.google.com/mail/u/0/')
