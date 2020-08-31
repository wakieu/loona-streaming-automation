# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def welcome_text():
    print('Hi, thanks for using my program :)\n')
    print('=====================================================\n')

def ask_login():
    pwd = ''
    email = input('Enter your e-mail or just press enter if you dont want to log in\n')
    if (email != ''):
        pwd = input('Enter the password (I swear im not stealing data)\n')
    return (email, pwd)

def login(info):
    if (info[0] != ''):
        driver.find_elements_by_css_selector('paper-button[aria-label*="Sign in"]')[0].click()
        driver.find_element_by_css_selector('input[type=email]').send_keys(info[0])
        driver.find_elements_by_css_selector('#identifierNext > div > button > div')[1].click()
        driver.find_element_by_css_selector('input[type=password]').send_keys(info[1])
        driver.find_elements_by_css_selector('#passwordNext > div > button > div')[1].click()
        time.sleep(2)
        try:
            driver.find_element_by_css_selector('#identity-prompt-confirm-button > span').click()
            time.sleep(4)
        finally:
            # nothing lol
            print('uhmmmm')

def ask_for_vid():
    # get the video you wanna stream
    vid = input('What video do you want to stream? (be specific)\n')
    if vid == '' : vid = 'you and i dreamcatcher'
    return vid

def watch_main_vid(vid):
    search_bar = driver.find_element_by_css_selector('input#search')
    search_bar.send_keys(vid)
    search_but = driver.find_element_by_css_selector('button#search-icon-legacy')
    search_but.click()
    # bot clicks the 1st result
    thumbnail = driver.find_elements_by_css_selector('a#video-title')[0]
    thumbnail.click()
    time.sleep(2)
    log_mv_info()
    watch_video()

def log_mv_info():
    print ('[' + time.strftime("%b %d %H:%M:%S", time.gmtime()) + ']')
    video_title = driver.find_element_by_css_selector('#container > h1').text
    print(video_title)
    views = driver.find_element_by_css_selector('#info-contents div#count').text
    print(views)
    print('=================================')

def video_cooldown():
    # ass
    driver.get('https://www.youtube.com/watch?v=846cjX0ZTrk') # HI HIGH
    watch_video()
    driver.get('https://www.youtube.com/watch?v=XEOCbFJjRw0') # BUTTERFLY
    watch_video()
    driver.get('https://www.youtube.com/watch?v=I5_BQAtwHws') # YOU AND I (DREAMCATCHER)
    watch_video()
    driver.get('https://www.youtube.com/watch?v=FKlGHHhTOsQ') # SCREAM (DREAMCATCHER)
    watch_video()

def to_sec(time):
    return int(int(time[0])*60+int(time[1]))

def watch_video_with_log():
    # bot uses stupid logic to wait for ads and the whole video
    duration= 0
    duration2 = 1
    while (duration != duration2 or duration2 < 60):
        ActionChains(driver).move_to_element(driver.find_element_by_css_selector('ytd-player#ytd-player')).perform()
        duration = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')
        duration = to_sec(duration)

        if (duration > 150):
            video_title = driver.find_element_by_css_selector('#container > h1').text
            print('Watching: ' + video_title)
            print('Duration:', duration)
            time.sleep(duration)
            break
        elif (duration >= 15):
            time.sleep(6)
            driver.find_element_by_css_selector('div.ytp-ad-skip-button-text').click()
            print('Skipped %s second ad' % duration)
        else:
            time.sleep(duration)
            print('Watched short ad (%s seconds)' % duration)

        ActionChains(driver).move_to_element(driver.find_element_by_css_selector('ytd-player#ytd-player')).perform()
        duration2 = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')
        duration2 = to_sec(duration2)

def watch_video():
    # bot uses stupid logic to wait for ads and the whole video
    duration= 0
    duration2 = 1
    while (duration != duration2 or duration2 < 60):
        ActionChains(driver).move_to_element(driver.find_element_by_css_selector('ytd-player#ytd-player')).perform()
        duration = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')
        duration = to_sec(duration)

        if (duration > 150):
            time.sleep(duration)
            break
        elif (duration >= 15):
            time.sleep(6)
            driver.find_element_by_css_selector('div.ytp-ad-skip-button-text').click()
        else:
            time.sleep(duration)

        ActionChains(driver).move_to_element(driver.find_element_by_css_selector('ytd-player#ytd-player')).perform()
        duration2 = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')
        duration2 = to_sec(duration2)

# EXECUTION
try:
    welcome_text()
    video = ask_for_vid()

    # config and setup the webdriver
    mute = webdriver.ChromeOptions()   
    mute.add_argument("--mute-audio")
    # bot will start and close a new window for each watch
    driver = webdriver.Chrome('.\\resources\\chromedriver', options=mute)
    driver.implicitly_wait(10)
    # bot goes to yt
    driver.get('https://www.youtube.com/')
    
    # main loop
    while (1):

        watch_main_vid(video)
        video_cooldown()

finally:
    # cleans the stuff
    if (driver != None) : driver.quit()

# cleans the stuff twice just to be sure
if (driver != None) : driver.quit()