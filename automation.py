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

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text) == "Thank you for attending"):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")