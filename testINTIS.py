from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

choice = input("Please select the mode for testing: 1 = Chrome, 2 = headless\n")
choice = int(choice)

if choice == 1:
    chrome = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    chrome.get('https://www.wikipedia.org/')
    searchItem ='Juraj Dobrila'

    language = chrome.find_element_by_xpath('//*[@id="searchLanguage"]/option[28]').click()

    search = chrome.find_element_by_xpath('//*[@id="searchInput"]').send_keys(searchItem)

    searchButton = chrome.find_element_by_xpath('//*[@id="search-form"]/fieldset/button').click()

    checkHistory = chrome.find_element_by_xpath('//*[@id="ca-history"]/a/span').click()

    filter = chrome.find_element_by_xpath('//*[@id="mw-history-search"]/legend/span[3]').click()

    date = chrome.find_element_by_xpath('//*[@id="ooui-1"]').click()

    elm = chrome.find_element_by_xpath('//*[@id="mw-input-date-range-to"]/div[2]/input')
    chrome.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", elm,"value", "2020-07-01")
    elm.click()
    chrome.find_element_by_xpath('//*[@id="ooui-php-7"]/button').submit()

    date_confirmation = chrome.find_element_by_xpath('//*[@id="pagehistory"]/li[1]/a')
    ##print(date_confirmation.text)
    if(date_confirmation.text) == "22:33, 24. travnja 2020.":
        print("Test is successfull")
    else:
        print("Test failed")
    time.sleep(20)
    chrome.close()

elif choice == 2:
    print("You are in headless mode")
    options = Options()
    options.headless = True
    chrome = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", options=options)
    chrome.get('https://www.wikipedia.org/')
    searchItem = 'Juraj Dobrila'

    language = chrome.find_element_by_xpath('//*[@id="searchLanguage"]/option[28]').click()

    search = chrome.find_element_by_xpath('//*[@id="searchInput"]').send_keys(searchItem)

    searchButton = chrome.find_element_by_xpath('//*[@id="search-form"]/fieldset/button').click()

    checkHistory = chrome.find_element_by_xpath('//*[@id="ca-history"]/a/span').click()

    filter = chrome.find_element_by_xpath('//*[@id="mw-history-search"]/legend/span[3]').click()

    date = chrome.find_element_by_xpath('//*[@id="ooui-1"]').click()

    elm = chrome.find_element_by_xpath('//*[@id="mw-input-date-range-to"]/div[2]/input')
    chrome.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", elm, "value", "2020-07-01")
    elm.click()
    chrome.find_element_by_xpath('//*[@id="ooui-php-7"]/button').submit()

    date_confirmation = chrome.find_element_by_xpath('//*[@id="pagehistory"]/li[1]/a')
    print(date_confirmation.text)
    if (date_confirmation.text) == "22:33, 24. travnja 2020.":
        print("Test is successfull")
    else:
        print("Test failed")
    time.sleep(15)
    chrome.close()

else:
    print("Provided answer is wrong")

