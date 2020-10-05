from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import numpy
 
buffer = []
activity = []
t = 180
 
op = Options()
op.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=op)
driver.create_options()
 
 
link = "https://www.youtube.com/watch?v=lM02vNMRRB0&ab_channel=NatureRelaxationFilms"
 
 
 
def startups():
    driver.get(link)
    driver.implicitly_wait(15)
    driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a").click()
    driver.implicitly_wait(15)
    frame = driver.find_element_by_xpath("/html/body/ytd-app/ytd-consent-bump-lightbox/paper-dialog/iframe")
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath("/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div").click()
    driver.switch_to_default_content()
 
 
    
def checkAds():
    try:
        ad_module = driver.find_element_by_class_name("ytp-ad-text")
        print("Waiting for ads to finish..")
        return True
    except NoSuchElementException:
        print("Ads finished! :D")
        return False
 
def setConditions(delay, downloadMb, uploadMb):
    driver.set_network_conditions(
    offline=False,
    latency=delay,  # additional latency (ms)
    download_throughput=downloadMb * 1024 * 128,  # maximal throughput
    upload_throughput=uploadMb * 1024 * 128)  # maximal throughput
 
def statsForNerds():
    source = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[1]/video")
    # action chain object
    action = ActionChains(driver)
    # right click operation
    action.context_click(source).perform()
    driver.find_element_by_xpath("//*[contains(text(), 'Statistik för nördar')]").click()
 
def endSession():
    driver.quit()
    print("-----------------------------")
    print("-----------------------------")
    print("-----------------------------")
    print("*reslutat*")
    print(buffer)
    print(activity)
 
def getData():
    for i in range(t):
        stats = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[19]")
        net = driver.find_element_by_css_selector("#movie_player > div.html5-video-info-panel > div > div:nth-child(10) > span > span:nth-child(2)").text
        net = net[:-3]
        activity.append(float(net))
        
        buf = driver.find_element_by_css_selector("#movie_player > div.html5-video-info-panel > div > div:nth-child(11) > span > span:nth-child(2)").text
        buf = buf[:-2]
        buffer.append(float(buf))
        time.sleep(0.3)
 
setConditions(delay=5, downloadMb=5, uploadMb=10)
startups()
while checkAds():
    time.sleep(1)
 
statsForNerds()
driver.implicitly_wait(15)
getData()
time.sleep(5)
endSession()