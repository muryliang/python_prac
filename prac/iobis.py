from selenium import webdriver
import time
import socks
import socket

img1="//img[@src='http://www.marinespecies.org/aphia/images/pnode.gif']"
img2="//img[@src='http://www.marinespecies.org/aphia/images/plastnode.gif']"
img3="//img[contains(@src, 'images/p')]"


#driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver = webdriver.Firefox()
time.sleep(2)
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
#socket.socket = socks.socksocket
driver.get("http://www.marinespecies.org/aphia.php?p=browser")
driver.implicitly_wait(60)
elems = driver.find_elements_by_xpath(img3)
elems.pop(0)
count = 0
try:
    while len(elems) !=  0:
        elems[0].click()
#            time.sleep(2.5)

        retry = 3
        while retry != 0:
            elems = driver.find_elements_by_xpath(img3)
            if len(elems) <= 1:
                retry -= 1
                print ("retrying")
                time.sleep(3)
                continue
            else:
                break

        if len(elems) <= 1:
                print ("no elems at all, break")
                break
        else:
            elems.pop(0)
            print ("got level1 elem", len(elems))
        count += 1
        print ("done,",count)

    print ("all over")
except Exception as e:
    print ("wrong and stop, saving...")

    with open("/tmp/done.html", "w") as f:
        f.write(driver.page_source)
    print ("write /tmp/done done")
