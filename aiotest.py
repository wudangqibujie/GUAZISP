HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    # "Cookie":"antipas=09pm9v3347x11E3344Fw6L2Z"
}
import time
import aiohttp
import requests
import asyncio
import multiprocessing as mp
from lxml import etree
url = "https://sz.lianjia.com/ershoufang/pg{}/"

async def getPage(p):
        async with aiohttp.ClientSession() as resp:
            async with resp.get(url.format(p),headers= HEADERS) as resp:
                page = await resp.text()
                get_data(page)
def get_data(page):
    html = etree.HTML(page)
    items = html.xpath('//ul[@class="sellListContent"]/li')
    data = [i.xpath('div[1]/div/a/text()') for i in items]
    print(data)

loop = asyncio.get_event_loop()
tasks = [getPage(i) for i in range(1,3)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
