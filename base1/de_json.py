import json
import sys
import re
import datetime

with open('temp.txt') as f: 
    data = f.read() 

data = data.replace("\'","\"").replace("None","\"None\"").replace("True","1").replace("False","0").replace("\\n",", ")

j_data = json.loads(data)

c_time = datetime.datetime.fromtimestamp(j_data['ctime']).strftime('%Y-%m-%d %H:%M:%S')
bais = j_data['stat']['view'] + 100 * j_data['stat']['like'] + 1000 * j_data['stat']['favorite'] + 1000 * j_data['stat']['coin'] + 1000 * j_data['stat']['share']
title = j_data['title']
desc = j_data['desc']

print(c_time + "\t" + str(bais) + "\t" + title + "\t" + desc)
