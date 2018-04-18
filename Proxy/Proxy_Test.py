import requests
import redis
import random
import time

class Test:
    def __init__(self):
        self.r = redis.Redis(host="localhost",port = "6379")
        self.url = "http://httpbin.org/ip"
    def view_ip(self,ip):
        proxy = {"http":ip,"https":ip}
        r = requests.get(self.url,proxies=proxy,timeout = 5)
        print(r.text)
    def create_ip(self,key_name):
        ip = self.r.srandmember(key_name,5)
        return [i.decode("utf-8") for i in ip]
    def run_test(self,key_name):
        t = Test()
        ip_list = t.create_ip(key_name)
        now = time.time()
        while True:
            print(ip_list)
            if time.time() != now + 100:
                try:
                    ip = random.choice(ip_list)
                    print("%s is testing"%ip)
                    self.view_ip(ip)
                except:
                    print("%s失效"%ip)
            else:
                ip_list = t.create_ip(key_name)
                now = time.time()

if __name__ == '__main__':
    a = Test()
    a.run_test("free_ip")

