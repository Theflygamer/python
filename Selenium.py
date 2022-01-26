from operator import imod
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\FrederikTeddyFlyPoin\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', chrome_options=options)
driver.get("https://www.twitch.tv/bu11en")
time.sleep(5)

find_chat = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div/ul/li[5]')
find_chat.click()
time.sleep(5)


js='$("textarea[aria-label*=\'Send en meddelelse\']").id = "dd"'
driver.execute_script(js)

#("alert('hey');$('textarea[aria-label*=\'Send en meddelelse\']').id = 'dd'")

time.sleep(1)
hit_chat= driver.find_element_by_id("dd")
hit_chat.click()
hit_chat.send_keys("!gamble 1000")
hit_chat.send_keys(Keys.RETURN)

