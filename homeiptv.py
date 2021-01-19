from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class homeiptv:
    def __init__(self,tvId,m3_url):
        self.tvId = tvId
        #self.m3ufile = m3ufile
        self.m3_url = m3_url
        self.bot = webdriver.Firefox()


    def automation(self):
        bot = self.bot
        bot.get('https://homeiptv.com/')
        time.sleep(2)


        tvId = bot.find_element_by_name('tvId')
        tvId.send_keys(self.tvId)
        time.sleep(2)

        #file = bot.find_element_by_name('file').send_keys('C:/Users/Daemon/Desktop/iptv.txt').click()
        

        m3_url = bot.find_element_by_name('m3_url')
        m3_url.send_keys(self.m3_url)
        time.sleep(1)
        
        SaveBTN = bot.find_element_by_xpath('//*[@id="finder-form-import"]/div/div[2]/div[3]/button').click()
        time.sleep(4)
        bot.close()


salah = homeiptv('11111111','https://google.com')
salah.automation()