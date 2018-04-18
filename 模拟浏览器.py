from selenium import webdriver
br = webdriver.PhantomJS()
url = "https://www.guazi.com/sz/dazhong/"
br.get(url)
import time
# time.sleep(6)
print(br.page_source)
