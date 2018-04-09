import subprocess
import shutil
import sys, os
import threading
import time

totalPolls=0.0
executions=0.0
maxUsers=0.0
minUsers=100000
count=0.0
sumation=0.0
maxi=0.0

results=open(sys.argv[1])
for line in results:
        splitit = line.split(" ")
        if (splitit[0] == "time:") :
                totalPolls += 1
                itime = float(splitit[1])
                sumation += itime
                if (itime > maxi):
                        maxi = itime
        elif (splitit[0] == "requests:") :
                executions += 1
                users = float(splitit[1])
                if (users > maxUsers):
                        maxUsers = users
                if (users < minUsers):
                        minUsers = users

#print "executions:" + str(executions)
#print "requests:" + str(totalPolls)
#print "max succeeded:" + str(maxUsers)
#print "min succeeded:" + str(minUsers)
#print "total request times:" + str(sumation)
print "polling user average:" + str(totalPolls/executions)
#print "average total time:" + str(sumation/executions)
#print "avg user time:" + str(sumation/totalPolls)
#print "max user time:" + str(maxi)
