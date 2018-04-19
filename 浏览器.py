from selenium import webdriver
chrome_opt = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images': 2}
chrome_opt.add_experimental_option('prefs',prefs)
br = webdriver.Chrome(chrome_options=chrome_opt)
url = "https://www.guazi.com/sz/dazhong/o{}/#bread"
import time
import multiprocessing as mp
from lxml import etree
def get_html(i):
    print(i)
    br.get(url.format(i))
    html = etree.HTML(br.page_source)
    title = html.xpath('//title/text()')
    print(title)
    br.close()
if __name__ == '__main__':

    li = [mp.Process(target=get_html,args = (i,)) for i in range(1,14)]
    for i in li:
        i.start()







