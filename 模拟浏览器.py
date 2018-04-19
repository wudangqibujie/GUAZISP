from lxml import etree
for i in range(1,14):
    f = open("大众{}.html".format(i),encoding = "utf-8")
    html = etree.HTML(f.read())
    items = html.xpath('//ul[@class="carlist clearfix js-top"]/li')
    print(items)
    for i in items:
        title = i.xpath('a/@title')
        link = i.xpath('a/@href')
        print(title)
        print(link)
