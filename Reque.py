HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    "Cookie":"antipas=09pm9v3347x11E3344Fw6L2Z"}
import time
import Data_Manage
import Url_Manager
import aiohttp
import asyncio
from lxml import etree
import logging
logging.basicConfig(level=logging.INFO)

class Req:
    def __init__(self):
        self.f = open("urls_task","a",encoding="utf-8")
        # self.tasks = urls
        self.new = Url_Manager.UrlManage()
    async def getPage(self,url):
            async with aiohttp.ClientSession() as resp:
                async with resp.get(url,headers= HEADERS) as resp:
                    page_source = await resp.text()
                    self.get_data(page_source)

    def get_data(self,page_source):
        item = Data_Manage.Item()
        txt_sto = Data_Manage.Data_Storage("page_data")
        html = etree.HTML(page_source)
        # if html.xpath('//ul[@class="pageLink clearfix"]'):
        #     link = html.xpath('//ul[@class="pageLink clearfix"]/li')
        #     logging.info(link)
        #     for i in link[:-1]:
        #         if i.xpath('a/@href'):
        #             n_url = i.xpath('a/@href')[0]
        #             logging.info("https://www.guazi.com"+n_url+"\n")
        #             self.f.write("https://www.guazi.com"+n_url+"\n")
        data_li = html.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for i in data_li:
            item["title"] = i.xpath('a/@title')
            item["link"] = i.xpath('a/@href')
            item["yrar_age"] = i.xpath('a/div[@class="t-i"]/text()')
            item["now_price"] = i.xpath('a/div[@class="t-price"]/p/text()')
            item["ex_price"] = i.xpath('a/div[@class="t-price"]/em/text()')
            txt_sto.TXT(item)
            logging.info(item)
        txt_sto.close_TXT()
    def run_async(self,urls):
        loop = asyncio.get_event_loop()
        tasks = [self.getPage(i) for i in urls]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
