from lxml import etree
import time
import logging
logging.basicConfig(level=logging.INFO)
import redis
import requests
class Mogu(object):
    def __init__(self):
        self.r = redis.Redis(host="localhost",port = "6379")
        self.url ="http://www.mogumiao.com/proxy/free/listFreeIp"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    def ip_list(self):
        r = requests.get(url=self.url,headers = self.headers)
        html = etree.HTML(r.text)
        ip_raw = eval(r.text)["msg"]
        # ip_raw = eval(r.text)["obj"]#这是正式购买后返回的格式调取
        ip_list = [i["ip"]+":"+i["port"] for i in ip_raw]
        return ip_list

    def free_set2redis(self,ip_list):
        for i in ip_list:
            self.r.sadd("free_ip",i)

    def clean_ip(self):
        for i in range(5):
            self.r.spop("free_ip")

    def free_run(self):
        m = Mogu()
        i = 0
        m.clean_ip()
        while True:
            i += 1
            ips = m.ip_list()
            m.free_set2redis(ips)
            print(i,ips)
            time.sleep(180)
            m.clean_ip()
if __name__ == '__main__':
    a = Mogu()
    a.free_run()
