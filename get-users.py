import threading
import time
import requests

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting "+self.name)
        savetofile(name)
        print("Exiting "+self.name)

def savetofile(filename):
        with open(filename,'w+') as f:
                for i in range(int(filename),int(filename)+2000):
                        p={"keyword":i}
                        h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
                        r=requests.get('https://www.luogu.com.cn/api/user/search',params=p,headers=h)
                        if(r.json()["users"]!=[None]):
                                f.write(r.text+'\n')

for i in range(0,1000000,2000):
        exec("thread%s=myThread(%d,'%s',%d)"%(i,i,i,i))
