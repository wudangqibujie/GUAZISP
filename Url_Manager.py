import redis

class UrlManage:
    def __init__(self):
        self.r = redis.Redis(host="localhost",port = "6379")
    def init_url_task(self,url):
        self.r.sadd("guazi_init_task",url)
    def new_url(self,newurl):
        self.r.sadd("new_task",newurl)
    def old_url(self,oldurl):
        self.r.sadd("old_task",oldurl)

