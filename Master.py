import requests

HEADERS = {
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    "Cookie":"antipas=09K9h3M347E1e1ub3344k62"
}
url = "https://www.guazi.com/bj?act=ajaxGetBrand"

class City:
    def city_data(self):
        r = requests.get(url,headers = HEADERS)
        r.encoding = "utf-8"
        f = open("car_id_data.txt","w",encoding="utf-8")
        f.write(r.text)
        f.close()
    def code2cz(self):
        city_data = []
        f = open("car_id_data.txt")
        da = eval(f.read().encode('latin-1').decode('unicode_escape'))
        
if __name__ == '__main__':
    m = City()
    data = m.code2cz()
    print(data)
