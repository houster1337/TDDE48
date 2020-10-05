from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import numpy

user = "mysan_msn@hotmail.com"
pw = "thornkung"

link1 = "https://www.netflix.com/watch/80049832?trackId=13752289&tctx=0%2C1%2C401005af3948a8aac06f03cbd686933592223c38%3Ad5d8f8d9e757e7e6ea3ff28c47c0484a79f94bbb%2C401005af3948a8aac06f03cbd686933592223c38%3Ad5d8f8d9e757e7e6ea3ff28c47c0484a79f94bbb%2Cunknown%2C"
link = "https://www.netflix.com"

op=Options()
op.add_argument("--incognito")
driver = webdriver.Chrome(options=op)

driver.create_options()

def start():
    driver.get(link1)
    driver.implicitly_wait(15)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/a").click()
    #driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/a").click()
    driver.implicitly_wait(15)
    driver.find_element_by_id("id_userLoginId").send_keys(user)
    driver.find_element_by_id("id_password").send_keys(pw)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/button").click()
    driver.implicitly_wait(15)  
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div").click()
    driver.implicitly_wait(15)  
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/div").click()

def getStats():
    send_keys(Keys.CONTROL, Keys.SHIFT, Keys.ALT, 'Q') # ??????????


def setConditions(delay, downloadMb, uploadMb):
    driver.set_network_conditions(
    offline=False,
    latency=delay,  # additional latency (ms)
    download_throughput=downloadMb * 1024 * 128,  # maximal throughput
    upload_throughput=uploadMb * 1024 * 128)  # maximal throughput

driver.set_network_conditions
setConditions(delay = 0, downloadMb=10, uploadMb=10)
start()
#time.sleep(2)
#getStats()

