import pymongo
import logging
import Url_Manager
logging.basicConfig(level=logging.INFO)
import requests
import Reque
import multiprocessing as mp
from lxml import etree
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    "Cookie":"antipas=09pm9v3347x11E3344Fw6L2Z"
}
class Master:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost",27017)
        # self.city = ["北京","上海","广州","深圳","重庆","江门","东莞","佛山","汕头","中山","珠海","天津"]
        self.city = ["郑州","西安","厦门","武汉","温州","太原","苏州","沈阳","南宁","南京","南昌","昆明","惠州","杭州","哈尔滨","福州","大连","成都","长沙","长春"]
        # self.car = ["奥迪","奔驰","宝马","保时捷","凯迪拉克","路虎","雷克萨斯","玛莎拉蒂","沃尔沃","英菲尼迪"]
        self.car = ["本田","别克","大众","福特","丰田","日产","现代","奥迪","奔驰","宝马","保时捷","凯迪拉克","路虎","雷克萨斯","玛莎拉蒂","沃尔沃","英菲尼迪"]
        # self.car = ["奥迪","阿尔法·罗密欧","奔驰","宝马","本田","别克","标致","保时捷","长城","大众","DS","福特","丰田","法拉利","哈弗","凯迪拉克","路虎","雷克萨斯","兰博基尼","劳斯莱斯","玛莎拉蒂","迈凯伦","日产","斯巴鲁","特斯拉","沃尔沃","现代","英菲尼迪","众泰"]
    def init_car_data(self):
        want_car = dict()
        db = self.client["guazi_data"]
        coll = db["guazi_car"]
        want_car = {k:next(coll.find({"name":k}))["url"] for k in self.car}
        logging.info(want_car)
        return want_car
    def init_city_data(self):
        want_city = dict()
        db = self.client["guazi_data"]
        coll = db["guazi_city"]
        want_city = {k:next(coll.find({"name":k}))["domain"] for k in self.city}
        logging.info(want_city)
        return want_city
    def create_init_url(self):
        u = Url_Manager.UrlManage()
        standard_url = "https://www.guazi.com/{city}/{car}/o1/"
        car_li = list(self.init_car_data().values())
        city_li = list(self.init_city_data().values())
        urls = [standard_url.format(city = i,car = j) for i in city_li for j in car_li]
        for i in urls:
             u.init_url_task(i)
        return urls
    def Parse_data(self):
        u = Url_Manager.UrlManage()
        req = Reque.Req()
        # urls = self.create_init_url()
        f = open("urls_task")
        urls = [i.strip() for i in f.readlines()]
        req.run_async(urls)

if __name__ == '__main__':
    m  = Master()
    m.Parse_data()
