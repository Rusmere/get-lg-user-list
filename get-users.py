import requests
import time
with open('lg_user.txt','w+') as f:
        for i in range(1000000):
                p={"keyword":i}
                h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
                r=requests.get('https://www.luogu.com.cn/api/user/search',params=p,headers=h)
                if(r.json()["users"]!=[None]):
                        f.write(r.text+'\n')
                        time.sleep(1)
