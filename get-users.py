import threading
import time
import requests
start=time.time()
for i in range(100,10000,100):
  for j in range(i-100,i):
    if(j==i-100):
      exec("file%s=open('%s','w+')"%(i,i))
    p={"keyword":j}
    h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    try:
      r=requests.get('https://www.luogu.com.cn/api/user/search',params=p,headers=h,timeout=15)
      if(r.json()["users"]!=[None]):
        print("Get UID:%s"%j)
        exec(r"file%s.write(r.text+'\n')"%(i))
        if(j==i):
          exec("file%s.close()"%i)
    except requests.exceptions.ConnectionError:
      print("Connection Error.")
end=time.time()
print("Done,Time=%d"%(end-start))
