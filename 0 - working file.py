import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
novel=res.text
k=open('三国演义.txt','a+')
k.write(novel)
k.close()