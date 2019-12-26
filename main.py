#coding=utf-8
import json
import requests

#请求地址
targetUrl = "https://ipinfo.io"

proxy_host = ''
proxy_port = ''

proxy_hub_url = 'https://api.proxyhub.cloud/v1/234d3446-6a7b-466a-b59b-4a50f0389be0/ip?format=json'
resp = requests.get(proxy_hub_url)
result = resp.text
obj = json.loads(result)
ips = obj.get('data')
print(ips)
for ip in ips:
    proxy_host = ip.get('ip')
    proxy_port = ip.get('port')
    if proxy_host is not None and proxy_port is not None:
        break

if proxy_host is None or proxy_port is None:
    print('no available ips')
    exit(-1)

proxy_info = "http://%(host)s:%(port)s" % {
    "host" : proxy_host,
    "port" : proxy_port,
}

#pip install -U requests[socks]  socks5代理
# proxy_info_socks5 = "socks5://%(host)s:%(port)s" % {
#     "host" : proxy_host,
#     "port" : proxy_port,
# }

proxies = {
    "http"  : proxy_info,
}
resp = requests.get(targetUrl, proxies=proxies)
# resp = requests.get(targetUrl)
# print(resp.status_code)
print(resp.text)
