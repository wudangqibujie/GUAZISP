import requests
import execjs
from lxml import etree
url = "https://www.guazi.com/sz/dc4bceaa77cf6144x.htm#fr_page=list&fr_pos=city&fr_no=1"
r = requests.get(url)
html = etree.HTML(r.text)
coo_fun = html.xpath('//script/text()')[0].strip()
print(coo_fun)
a = execjs.compile(coo_fun+"function A(){return value;}")
print(a.call("A"))
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    "Cookie":"antipas=09K9h3M347E1e1ub3344k62"
}
HEADERS1 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    # "Cookie":"antipas=23355186Dw913073712X60DE78d"
}
s = requests.Session()
r1 = s.get(url,headers = HEADERS)
html1 = etree.HTML(r1.text)
print(r1.status_code)
title = html1.xpath('//title/text()')
print(title)
r2 = s.get("https://www.guazi.com/sz/be1caa8fe1d2cb77x.htm#fr_page=list&fr_pos=city&fr_no=2",headers=HEADERS1)
print(r2.status_code)

