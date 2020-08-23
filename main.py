# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# get the video you wanna stream
vid = input('What video do you want to stream? (be specific)\n')
if vid == '' : vid = 'loona butterfly mv'

# config and setup the webdriver
mute = webdriver.ChromeOptions()   
mute.add_argument("--mute-audio")

# main loop
try:
    while (1):
        # bot will start and close a new window for each watch
        driver = webdriver.Chrome('.\\resources\\chromedriver', options=mute)
        driver.implicitly_wait(10)

        # bot goes to yt and searches for the video
        driver.get('https://www.youtube.com/')
        search_bar = driver.find_element_by_css_selector('input#search')
        search_bar.send_keys(vid)
        search_but = driver.find_element_by_css_selector('button#search-icon-legacy')
        search_but.click()

        # bot clicks the 1st result
        thumbnail = driver.find_elements_by_css_selector('a#video-title')[0]
        thumbnail.click()
        time.sleep(2)

        # bot does not like if its not loona
        channel = driver.find_element_by_css_selector('div#upload-info a').text
        print(channel)
        if (channel != 'loonatheworld') : raise Exception('not loona smh')

        # bot uses stupid logic to wait for ads and the whole video
        duration= 0
        duration2 = 1
        while (duration != duration2):
            ActionChains(driver).move_to_element(driver.find_element_by_css_selector('ytd-player#ytd-player')).perform()
            duration = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')

            print(duration)
            a = int(int(duration[0])*60+int(duration[1]))
            print(a)
            time.sleep(a+1)
            if (a > 100) : break

            ActionChains(driver).move_to_element(driver.find_element_by_css_selector('ytd-player#ytd-player')).perform()
            duration2 = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')

        # bot click another video to pretend its not a bot
        driver.find_element_by_css_selector('ytd-compact-radio-renderer + ytd-compact-video-renderer').click()
        time.sleep(45)

        # closes the page, ready to watch again
        driver.quit()

finally:
    # cleans the stuff
    if (driver != None) : driver.quit()