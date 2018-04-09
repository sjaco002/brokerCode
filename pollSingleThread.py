import subprocess
import shutil
import sys, os
import threading
import time
import pycurl
import json
from time import sleep

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

c = pycurl.Curl()

i=0
j=0
iterations=10
maxUsers = 1000
while (j<iterations):
        locations=open("UserLocations.adm")
        i=0
        start = time.time()
        for line in locations:
                i=i+1
                trimmedLine = line.split("\"")
                location = trimmedLine[7]
                location = location.replace(" ","%20")
                url="http://promethium.ics.uci.edu:19002/query/service"
                command = "select%20r%2Cshelters%20from%20steven.Reports%20r"
                command += "%20let%20shelters%20=%20(select%20s.location%20from%20steven.Shelters%20s%20where%20spatial_intersect(s.location%2Ccircle('"
                command += location + "')))"
                command += "%20where%20r.timeStamp%20>%20current_datetime()%20-%20day_time_duration('PT10S')"
                command += "%20and%20spatial_intersect(r.location%2Ccircle('"
                command += location + "'))%3B"
                data=json.dumps({"statement":command})
                c.setopt(pycurl.URL,url)
                c.setopt(pycurl.POST, 1)
                c.setopt(pycurl.POSTFIELDS, data)
                c.perform()
                print('time: %f' % c.getinfo(c.TOTAL_TIME))
                elapsed = time.time() - start
                if (i >= maxUsers):
                    while (elapsed < 10):
                        elapsed = time.time() - start
		if (elapsed >= 10):
                    print('requests: %f' % i)
                    break
        j=j+1
c.close()
