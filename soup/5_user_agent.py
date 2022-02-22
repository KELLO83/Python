import requests

url="http://nadocoding.tistory.com"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/97.0.4692.71 Safari/537.36"}

res=requests.get(url,headers=headers)

with open("nadocoding.htm","w",encoding="utf8") as f:
    
    f.write(res.text)
    
        