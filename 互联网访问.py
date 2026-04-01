
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import urllib.error
# response = urlopen('https://www.example.com')
# data = response.read().decode('utf-8')  # 读取并解码为字符串
# print(data)

#
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
#
# Beware the Ides of March.
# """)
# server.quit()

import requests

response = requests.get('http://10.1.14.26:5173/settleIn#/login', verify=False)  # 不验证 SSL 证书（不推荐）
# 或者指定 CA 证书文件路径（推荐）
# response = requests.get('https://your-url.com', verify='/path/to/your/cacert.pem')

print(response)