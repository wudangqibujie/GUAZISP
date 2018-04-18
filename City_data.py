url = "https://www.guazi.com/sz/?act=ajaxGetOpenCity"
import requests
import json
import pymongo
HEADERS = {
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291",
    "Cookie":"antipas=09K9h3M347E1e1ub3344k62"
}
class City:
    def city_data(self):
        r = requests.get(url,headers = HEADERS)
        r.encoding = "utf-8"
        f = open("city_id_data.txt","w",encoding="utf-8")
        f.write(r.text)
        f.close()
    def code2cz(self):
        city_data = []
        f = open("city_id_data.txt")
        da = eval(f.read().encode('latin-1').decode('unicode_escape'))
        # da1 = list(da["data"]["cityList"]["all"].values())[0][0]["pinyin"]
        da1 = list(da["data"]["cityList"]["all"].values())
        for i in da1:
            for j in i:
                if "id" in j:
                    data_dict = dict()
                    data_dict["id"]=j["id"]
                    data_dict["name"] = j["id"]
                    data_dict["domain"] = j["domain"]
                    data_dict["pinyin"] = j["pinyin"]
                    data_dict["location"] = j["location"]
                    data_dict["city_code"] = j["city_code"]
                    city_data.append(data_dict)
        return city_data
    def cityda2mongo(self):
        client = pymongo.MongoClient("localhost",27017)
        db = client["guazi_data"]
        coll = db["guazi_city"]
        for i in self.code2cz():
            coll.insert(i)


if __name__ == '__main__':
    a = City()
    a.cityda2mongo()


