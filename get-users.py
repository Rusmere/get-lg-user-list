import threading
import time
import requests
for i in range(0,1000,200):
  for j in range(i-200,i):
    exec("file%s=open('%s','w+')"%(i,i))
    p={"keyword":j}
    h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    try:
      r=requests.get('https://www.luogu.com.cn/api/user/search',params=p,headers=h)
      if(r.json()["users"]!=[None]):
        print("UID:%s"%j)
        exec(r"file%s.write(r.text),'\n'"%(i))
    except TimeoutError:
      exec("file%s.close()"%i)
