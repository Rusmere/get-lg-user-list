import time
import requests
from requests.adapters import HTTPAdapter
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=4))
s.mount('https://', HTTPAdapter(max_retries=4))
start=time.time()
for i in range(320000,360000,20000):
  for j in range(i-20000,i):
    if(j==i-20000):
      exec("file%s=open('%s','w+')"%(i,i))
    p={"keyword":j}
    h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    try:
      r=s.get('https://www.luogu.com.cn/api/user/search',params=p,headers=h,timeout=15)
      if(r.json()["users"]!=[None]):
        print("Get UID:%s"%j)
        exec(r"file%s.write(r.text+'\n')"%(i))
        if(j==i):
          exec("file%s.close()"%i)
    except requests.exceptions.ConnectionError:
      print("Connection Error.")
    except socket.timeout:
      print("Socket timeout.")
      
print("Done,Time=%d"%(float(time.time())-start))
