# 易查分微信小程序爬虫
# Author: wzx1210
# Date: 2022-11-27
# Version: 1.0
# Path: score_spider.py
# input: ./input.xls
# input format: [class, name, id] without header
# output: ./result.xls
# output format: [class, name, id, scoreA, scoreB, scoreC, ...] without header

import requests
import json
from urllib import parse
import xlwt
import xlrd


def query(name, id):
    url = "https://www.yichafen.com/Miniprogram/Index/verifyParams?kkey=******** "
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    }
    params = {
        "s_xingming": '',
        "s_xuehao": '',
        "sqcode": "********",
    }
    params['s_xingming'] = name
    params['s_xuehao'] = id
    res = requests.get(url=url, headers=headers, params=params)
    try:
        token = json.loads(res.text)['data']['token']
    except KeyError:
        return None
    else:
        url = "https://www.yichafen.com/Miniprogram/Index/queryResult?token="
        url = url+token
        res = requests.get(url=url, headers=headers).text.encode(
            'utf-8').decode("unicode_escape")
        # print(res)
        fmt = json.loads(res)['data']['recordList'][0]['columnList']
        return fmt


if __name__ == "__main__":
    rd = xlrd.open_workbook('./input.xls').sheet_by_index(0)
    wb = xlwt.Workbook(encoding='utf-8', style_compression=0)
    ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)
    for rown in range(rd.nrows):
        name = rd.cell_value(rown, 1)
        id = rd.cell_value(rown, 2)
        id = str(id)[0:-2]
        res = query(name=name, id=id)
        if res is None:
            ws.write(rown, 0, rd.cell_value(rown, 0))
            ws.write(rown, 1, name)
            ws.write(rown, 2, id)
            print(name+id+" query failed")
            continue
        for i in range(8):
            ws.write(rown, i, res[i]['value'])
            wb.save('result.xls')

        print(name+id+" ok")
