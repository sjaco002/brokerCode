import subprocess
import shutil
import sys, os
import threading
import time
import pycurl
import json
import cStringIO
from time import sleep

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

c = pycurl.Curl()
b = cStringIO.StringIO()

i=0
j=0
iterations=10
maxUsers = 1100
while (j<iterations):
        locations=open("UserLocations.adm")
        i=0
        start = time.time()
        for line in locations:
                i=i+1
                trimmedLine = line.split("\"")
                location = trimmedLine[7]
                url="http://promethium.ics.uci.edu:19002/query/service"
                command = "select r, shelters from steven.Reports r"
                command += " let shelters = (select s.location from steven.Shelters s where spatial_intersect(s.location,circle('"
                command += location + "')))"
                command += " where r.timeStamp > current_datetime() - day_time_duration('PT10S')"
                command += " and spatial_intersect(r.location,circle('"
                command += location + "'));"
                data=json.dumps({"statement":command})
                c.setopt(pycurl.URL,url)
                c.setopt(pycurl.POST, 1)
                c.setopt(pycurl.POSTFIELDS, command)
                c.setopt(c.WRITEFUNCTION, b.write)
                c.perform()
                print b.getvalue()
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
