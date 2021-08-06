import requests

BASE = "http://127.0.0.1:5000/"


data = [
    {"likes":10,"name":"First video","views":10},
    {"likes":10,"name":"Sec video","views":11},
    {"likes":10,"name":"Thr video","views":12},
]

for i in range (len(data)):    
    response= requests.put(BASE+"video/"+str(i),data[i])
    print(response.json())

input()
response= requests.get(BASE+"video/1")  
print(response.json())