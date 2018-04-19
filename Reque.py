HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    # "Cookie":"antipas=09pm9v3347x11E3344Fw6L2Z"
}
import time
import Data_Manage
import Url_Manager
import aiohttp
import asyncio
from lxml import etree
import logging
logging.basicConfig(level=logging.INFO)

class Req:
    def __init__(self,urls):
        self.tasks = urls
        self.new = Url_Manager.UrlManage()
    async def getPage(self,url):
            async with aiohttp.ClientSession() as resp:
                async with resp.get(url,headers= HEADERS) as resp:
                    page = await resp.text()
                    self.get_data(page)

    def get_data(self,page):
        item = Data_Manage.Item()
        txt_sto = Data_Manage.Data_Storage()
        html = etree.HTML(page)
        new_next = html.xpath('//ul[@class="pageLink clearfix"]')
        if new_next:
            link = new_next.xpath('li[-1]/a/@href')
            self.new.new_url("https://www.guazi.com"+link)
            logging.info("https://www.guazi.com"+link)
        data_li = html.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for i in data_li:
            item["title"] = i.xpath('a/@title')
            item["link"] = i.xpath('a/@href')
            item["yrar_age"] = i.xpath('a/div[@class="t-i"]/text()')
            item["now_price"] = i.xpath('a/div[@class="t-price"]/p/text()')
            item["ex_price"] = i.xpath('a/div[@class="t-price"]/em/text()')
            txt_sto.TXT(item)
        txt_sto.close_TXT()



    def run_async(self,urls):
        loop = asyncio.get_event_loop()
        tasks = [self.getPage(i) for i in self.tasks]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
