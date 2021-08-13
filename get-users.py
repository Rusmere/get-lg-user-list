import threading
import time
import requests
for i in range(0,1000,200):
  exec("file%s=open('%s','w+')"%(i,i))
  p={"keyword":i}
  h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
  try:
    r=requests.get('https://www.luogu.com.cn/api/user/search',params=p,headers=h)
    if(r.json()["users"]!=[None]):
      print("UID:%s"%i)
      exec("file%s.write(r.text,'\n')"%(i))
  except TimeoutError:
    exec("file%s.close()"%i)
