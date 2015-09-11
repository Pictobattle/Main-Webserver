import httplib, urllib

conn = httplib.HTTPConnection("localhost:8080")
body=[]
headers=[]
conn.request("GET", "/", body, headers)
response = conn.getresponse()
conn.close()

print(response)
