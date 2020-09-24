from selenium import webdriver


def useSelenium(browser, url):
    browser = webdriver.Firefox(executable_path=r'C:/Users/HP/AppData/Local/Programs/Python/Python36/BrowersDriver/geckodriver.exe')
    browser.get(url)
    try:
        elem = browser.find_element_by_class_name('card-img-top')
        print('Found <%s> element with that class name !' % (elem.tag_name))
    except:
        print('Was able to find none')


def clickElemen(url):
    browser = webdriver.Firefox(executable_path=r'C:/Users/HP/AppData/Local/Programs/Python/Python36/BrowersDriver/geckodriver.exe')
    browser.get(url)
    try:
        linkElem = browser.find_element_by_link_text('Buy Print/Ebook Bundle')
        print('Element clicked')
    except:
        print('no Element clicked')
    type(linkElem)
    linkElem.click()


url = 'http://inventwithpython.com'
clickElemen(url)
#useSelenium(url)
