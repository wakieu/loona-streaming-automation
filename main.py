# pip install selenium

from selenium import webdriver
import time

vid = 'nct 127'
# vid = input('What video do you want to stream? (be specific)\n')
if vid == '' : vid = 'bruh sound effect'

driver = webdriver.Chrome('.\\resources\\chromedriver')
driver.implicitly_wait(10)
driver.get('https://www.youtube.com/')

search_bar = driver.find_element_by_css_selector('input#search')
search_bar.send_keys( vid )
search_but = driver.find_element_by_css_selector('button#search-icon-legacy')
search_but.click()

thumbnail = driver.find_elements_by_css_selector('a#video-title')[0]
thumbnail.click()
time.sleep(2)
channel = driver.find_element_by_css_selector('ytd-channel-name#channel-name a').text
print(channel)
duration= 0
duration2 = 1
while (duration != duration2):
    duration = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')

    print(duration)
    a = int(int(duration[0])*60+int(duration[1]))
    print(a)
    time.sleep(a)

    duration2 = driver.find_element_by_css_selector('span.ytp-time-duration').text.split(':')

#replay = driver.find_element_by_css_selector('button[title="Replay"]')

driver.close()