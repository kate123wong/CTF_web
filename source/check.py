import re
import requests
import base64
#发送url
url = 'http://127.0.0.1:5000'
response = requests.get(url)
print(response.headers)

