import subprocess
import shutil
import sys, os
import threading
import time

results=open("responses/responses.txt")
count=0.0
sumation=0.0
records=0.0
first=True
for line in results:  
        trimmedLine = line.split("\"")
        if (len(trimmedLine) != 1):
                if (first == False):
                        records += 1.0
                continue
        try:
                float(line)
        except ValueError:
                continue
        if (first):
                first=False
                continue
        count += 1.0
        sumation += float(line)
print count 
print sumation 
print (sumation/count)
print (records/count)
