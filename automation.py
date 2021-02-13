from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://en.savefrom.net/sf')

time.sleep(2)

thisLink= input('Enter the Link:')
linkOperation = web.find_element_by_xpath('//*[@id="sf_url"]')
linkOperation.send_keys(thisLink)

Submit = web.find_element_by_xpath('//*[@id="sf_submit"]')
Submit.click()


try:
    toDownload  = web.find_element_by_xpath('//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
    toDownload.click()
    print('Download Completed!')
except:
    print('Error!')
