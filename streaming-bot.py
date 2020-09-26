# pip install selenium

from selenium import webdriver
import time

player = 'ytd-player#ytd-player'
skip_countdown = 'span.countdown-next-to-thumbnail'
skip_container = 'span.ytp-ad-skip-button-container'
skip_button = 'div.ytp-ad-skip-button-text'
video_duration = 'span.ytp-time-duration'
autoplay_toggle = 'div#toggleButton'
autoplay_active = 'paper-toggle-button[aria-pressed="true"]'
search_bar = 'input#search'
search_button = 'button#search-icon-legacy'
video_title = '#container > h1'
views_count = '#info-contents div#count'
other_videos = 'span#video-title'

def element(locator):
    try:
        return driver.find_element_by_css_selector(locator)
    except:
        return

def elements(locator):
    try:
        return driver.find_elements_by_css_selector(locator)
    except:
        return

def has_element(locator):
    try:
        driver.implicitly_wait(2)
        return element(locator)
    except:
        driver.implicitly_wait(10)
        return False
    finally:
        driver.implicitly_wait(10)

def has_ad():
    return has_element('div[id*=simple-ad-badge]')

def handle_ads():
    if (has_ad()):
        if (has_element(skip_container)):
            element(skip_button).click()
        else:
            time.sleep(getDuration())
        time.sleep(1)
        handle_ads()

def to_sec(time):
    aux = time.split(':')
    minutes = int(aux[0])*60
    seconds = int(aux[1])
    return minutes + seconds

def getDuration():
    ret = driver.find_element_by_css_selector(video_duration).get_attribute('innerHTML')
    if (':' in ret):
        return to_sec(ret)

def disable_autoplay():
    if (has_element(autoplay_active)):
        element(autoplay_toggle).click()

def welcome_text():
    print('Hi, thanks for using my program :)\n')
    print('=====================================================\n')

def ask_for_vid():
    vid = input('What video do you want to stream? (be specific)\n')
    if vid == '' :
        print('Nothing was typed...\n')
        return ask_for_vid()
    return vid

def goto_vid(vid):
    element(search_bar).clear()
    element(search_bar).send_keys(vid)
    element(search_button).click()
    time.sleep(3)
    elements('a#video-title')[0].click()

def getTitle():
    video_title_text = element(video_title).text
    if (video_title_text == ''):
        return getTitle()
    return video_title_text

def getViews():
    views = element(views_count).text
    if (views == ''):
        return getViews()
    return views

def log_info():
    time.sleep(1)
    print ('[' + time.strftime("%b %d %H:%M:%S", time.gmtime()) + ']')
    print(getTitle())
    print(getViews())
    print('=================================')

def small_log():
    time.sleep(1)
    print(getTitle())
    print('---------------------------------')

def watch_video():
    handle_ads()
    time.sleep(getDuration())

def watch_video_and_log():
    handle_ads()
    log_info()
    time.sleep(getDuration())

def watch_video_small_log():
    handle_ads()
    small_log()
    time.sleep(getDuration())

def video_cooldown():
    driver.get('https://www.youtube.com/watch?v=846cjX0ZTrk') # HI HIGH
    watch_video()
    driver.get('https://www.youtube.com/watch?v=XEOCbFJjRw0') # BUTTERFLY
    watch_video()
    driver.get('https://www.youtube.com/watch?v=I5_BQAtwHws') # YOU AND I (DREAMCATCHER)
    watch_video()
    driver.get('https://www.youtube.com/watch?v=FKlGHHhTOsQ') # SCREAM (DREAMCATCHER)
    watch_video()

def look_for_next(videos):
    for index, video in enumerate(videos):
        title = video.text
        if ('LOONA' in title or 'Dreamcatcher' in title):
            return index
    return False

def video_cooldown2():
    t = 0
    while (t < 900):
        side_videos = elements(other_videos)
        next_vid = look_for_next(side_videos)
        if (next_vid or next_vid == 0):
            side_videos[next_vid].click()
        else:
            side_videos[3].click()
        time.sleep(3)
        watch_video_small_log()
        d = getDuration()
        t += d


# EXECUTION
try:
    welcome_text()
    video = ask_for_vid()

    # config and setup the webdriver
    mute = webdriver.ChromeOptions()   
    mute.add_argument("--mute-audio")
    # bot will start and close a new window for each watch
    driver = webdriver.Chrome('.\\resources\\chromedriver', options=mute)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # bot goes to yt
    driver.get('https://www.youtube.com/')
    print('\n=================================')
    # main loop
    while (1):
        goto_vid(video)
        disable_autoplay()
        watch_video_and_log()
        video_cooldown2()

finally:
    # cleans the stuff
    if (driver != None) : driver.quit()

# cleans the stuff again just to be sure
if (driver != None) : driver.quit()