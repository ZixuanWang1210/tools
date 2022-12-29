# oierdb 自动查询
# Author: wzx1210
# Date: 2022-10-1
# Version: 1.0
# Path: ioerdb_spider.py
# input: standard input name
# output: standard output prize

import json
import urllib.parse
import urllib.request

while 1:
    name = input()
    print(name)
    chName = urllib.parse.quote(name)
    url = 'https://bytew.net/OIer/search.php?method=normal&q=%s' % (chName)
    result = urllib.request.urlopen(url)
    data = json.loads(result.read())

    for person in data['result']:
        if person['name'] != name:
            continue
        if int(person['year']) < 2015:
            continue
        if int(person['year']) > 2016:
            continue

        print(person['name'], person['year'])
        award = eval(person['awards'])
        for x in award:
            print(x['province'], x['identity'], x['award_type'])