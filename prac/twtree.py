from selenium import webdriver
import time


#driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver = webdriver.Firefox()
driver.get("http://fishdb.sinica.edu.tw/AjaxTree/tree.php")
driver.implicitly_wait(60)

elem = driver.find_element_by_xpath("//div[contains(@style, 'plus')]")
count = 0
while elem:
    elem.click()
    elem = driver.find_element_by_xpath("//div[contains(@style, 'plus')]")
    count += 1
    print ("done %d times"%(count))
print ("done")
