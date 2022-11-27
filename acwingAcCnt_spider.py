# Acwing 刷题统计
# Author: wzx1210
# Date: 2020-11-5
# Version: 1.0
# Path: acwingAcCnt_spider.py
# input: None
# output: stand output count

import requests
s = requests.Session()
c = {
    'csrftoken': '**********',
    'sessionid': '**********',
}
baseurl = 'https://www.acwing.com/problem/'
cnt = 0
for i in range(1, 97):
    url = baseurl+str(i)+'/'
    r = requests.get(url, cookies=c)
    resp = r.text
    cnt += resp.count("已通过这道题目")
print(cnt)
