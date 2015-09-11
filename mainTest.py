import httplib, urllib

conn = httplib.HTTPConnection("localhost:8080")
conn.request("GET", "/")
response = conn.getresponse()
conn.close()

return response
