from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import numpy as np
 
buffer = []
activity = []
t = 180
op = Options()
op.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=op)
driver.create_options()

link = "https://www.youtube.com/watch?v=lM02vNMRRB0&ab_channel=NatureRelaxationFilms"
 
# Starts a chrome webdriver and loads a youtube video, implicitly waits and then dismisses the popups.
def startup():
    driver.get(link)
    driver.implicitly_wait(15)
    driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a").click()
    driver.implicitly_wait(15)
    frame = driver.find_element_by_xpath("/html/body/ytd-app/ytd-consent-bump-lightbox/paper-dialog/iframe")
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath("/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div").click()
    driver.switch_to_default_content()

# Checks if youtube ads are playing.
def checkAds():
    try:
        ad_module = driver.find_element_by_class_name("ytp-ad-text")
        print("Waiting for ads to finish..")
        return True
    except NoSuchElementException:
        print("Ads finished! :D")
        return False
 
# Call set conditions to throttle throughput or add latency.
def setConditions(delay, downloadMb, uploadMb):
    driver.set_network_conditions(
    offline=False,
    latency=delay,  # additional latency (ms)
    download_throughput=downloadMb * 1024 * 128,  # maximal throughput
    upload_throughput=uploadMb * 1024 * 128)  # maximal throughput
# Toggle the stats for nerds display.
def statsForNerds():
    source = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[1]/video")
    # action chain object
    action = ActionChains(driver)
    # right click operation
    action.context_click(source).perform()
    driver.find_element_by_xpath("//*[contains(text(), 'Statistik för nördar')]").click()

# Collects network activity and buffer size data roughly 3 times per second and stores it in the buffer and activity variables.
def collectData():
    for i in range(t):
        stats = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[19]")
        net = driver.find_element_by_css_selector("#movie_player > div.html5-video-info-panel > div > div:nth-child(10) > span > span:nth-child(2)").text
        net = net[:-3]
        activity.append(float(net))
        
        buf = driver.find_element_by_css_selector("#movie_player > div.html5-video-info-panel > div > div:nth-child(11) > span > span:nth-child(2)").text
        buf = buf[:-2]
        buffer.append(float(buf))
        time.sleep(0.3)

# Saves the data and prints out the mean buffer size [s] and mean network activity [KB]. 
# Also exits the driver.
def endSession():
    npBuffer = np.array(buffer)
    npActivity = np.array(activity)
    print("-----------------------------")
    print("-----------------------------")
    print("-----------------------------")
    print("*Results*")
    print("Mean buffer size: "+str(np.mean(npBuffer)))
    print("Mean network activity: "+str(np.mean(npActivity)))
    fBuff = open("BadBuff.txt", "w")
    fBuff.write(str(buffer))
    fBuff.close()
    fNet = open("BadNet.txt", "w")
    fNet.write(str(activity))
    fNet.close()
    driver.quit()

# Remove if you want to run the script without virtual limitations.
setConditions(delay=500, downloadMb=1, uploadMb=1)
startup()
## Checks if any ads are running to avoid them interferring with the experiment.
while checkAds():
    time.sleep(1)

statsForNerds()
driver.implicitly_wait(15)
collectData()
time.sleep(5)
endSession()