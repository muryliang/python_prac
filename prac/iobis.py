from selenium import webdriver
import time

img1="//img[@src='http://www.marinespecies.org/aphia/images/pnode.gif']"
img2="//img[@src='http://www.marinespecies.org/aphia/images/plastnode.gif']"

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
#driver = webdriver.Firefox()
time.sleep(2)
driver.get("http://www.marinespecies.org/aphia.php?p=browser")
driver.implicitly_wait(60)
elems = driver.find_elements_by_xpath(img1)
elems.pop(0)
count = 0
try:
    while len(elems) !=  0:
            elems[0].click()
            time.sleep(2.5)

            retry = 3
            while retry != 0:
                elems = driver.find_elements_by_xpath(img1)
                if len(elems) <= 1:
                    retry -= 1
                    print ("retrying")
                    time.sleep(3)
                    continue
                else:
                    break

            if len(elems) <= 1:
                print ("level1 after retry still zero")
                retry = 3
                while retry != 0:
                    elems = driver.find_elements_by_xpath(img2)
                    if len(elems) == 0:
                        retry -= 1
                        print ("retrying level2")
                        time.sleep(3)
                        continue
                    else:
                        break

                if len(elems) == 0:
                    print ("no elems at all, break")
                    break
                else:
                    print ("got level2 elem", len(elems))
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
