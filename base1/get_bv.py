import urllib
import urllib.request
import re
import os

def GetHTML(url):
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
    request = urllib.request.Request(url, headers = header)
    response = urllib.request.urlopen(request)
    h = response.read().decode('utf-8')
    return h
    
def GetInfo(h):
    pattern = r'href="//www.bilibili.com/video/BV[^/]+/'
    bvs = re.findall(pattern, h)
    return bvs
    
#h = GetHTML('https://search.bilibili.com/all?vt=70359611&keyword=%E4%B8%81%E7%9C%9F&from_source=webtop_search&spm_id_from=333.1007&search_source=6')
#h = GetHTML('https://search.bilibili.com/all?vt=70359611&keyword=%E4%B8%81%E7%9C%9F&from_source=webtop_search&spm_id_from=333.1007&search_source=6&page=2')
for k in range(1, 34):
    h = GetHTML('https://search.bilibili.com/all?keyword=%E4%B8%80%E7%9C%BC%E4%B8%81%E7%9C%9F&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page={}'.format(k))
    bvs = GetInfo(h)
    for bv in bvs:
        print(bv[31:43])