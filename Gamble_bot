from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\\FrederikTeddyFlyPoin\\AppData\\Local\\Google\\Chrome\\User Data\\Default")# this make sure you open a browser you have login to (you need to login first time) 
options.add_argument('window-size=2048x1152')
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', chrome_options=options)
driver.get("https://www.twitch.tv/bu11en")
time.sleep(5)

try:
        find_chat = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div/ul/li[5]')
        find_chat.click()
except NoSuchElementException:
    pass

#find_chat=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div/ul/li[5]')
#find_chat.click()
#time.sleep(5)

i=0
while i <= 10:
    hit_chat= driver.find_element_by_tag_name('textarea')
    hit_chat.click()
    hit_chat.send_keys("!gamble 232323")
    hit_chat.send_keys(Keys.RETURN)
    print ("Gamble done, Cooldown starts now ")
    for i in range(46,0,-1):
        time.sleep(1)
        print (i)
driver.exit();
