class Item(dict):
    def __init__(self):
        pass
if __name__ == '__main__':
    a = Item()
    a["name"] = "宝马"
    a["link"] = "www.bai"
    print(a)
class Data_Storage:
    def __init__(self,file_name):
        self.f = open(file_name+".txt","w",encoding="utf-8")
    def TXT(self,item_data):
        self.f.write(str(item_data)+"\n")
    def close_TXT(self):
        self.f.close()

if __name__ == '__main__':
    d = Data_Storage("guazi")
    d.TXT({"A":"B"})
    d.close_TXT()
