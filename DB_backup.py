#!/usr/bin/python3

import os
import sys
import datetime

#vars
mounted = True
share_host = ("fs.localhost")
share_point = ("/ifs/PGdump")
mount_point = ("/mnt/backup")
check_mount = (share_host + ":" + share_point + " on " + mount_point)

endfix = ("dump")
expire = 7

# check mount - file in share
call = os.system("ls  %s/_MOUNTED_" % (mount_point))
mounted = bool(call)

if not mounted:
        print("mount: OK")
else:
        print("mount: NOT")
        sys.exit(1)

#date
now = datetime.datetime.now()

#fuction
def strData(t0):
        tY = int(t0[0:4])
        tM = int(t0[4:6])
        tD = int(t0[6:8])
        d0 =  datetime.date(tY, tM, tD)
        return d0

def ileDni(d0, t0):
        d1 = d0 - datetime.timedelta(days = t0)
        return d1

teraz = strData(now.strftime("%Y") + now.strftime("%m")+ now.strftime("%d"))
do_daty = ileDni(teraz, expire)

#databases list
databases = ['bugzilla', 'confluence', 'crucible', 'datadigger', 'geoportal', 'jiradb', 'models', 'picocms', 'postgres', 'template0', 'template1']

#list directory
tmp =[]
for path in os.listdir(mount_point):
        tmp.append(path)

#list file with dump endfix
items = []
for i in tmp:
        if i.endswith((endfix)):
                items.append(i)

for d in databases:
        call = os.system("echo pg_dump -U backup -F d -f %s/%s_%s.%s %s" % (mount_point, d, (now.strftime("%Y") + now.strftime("%m")  + now.strftime("%d")), endfix, d ))

        tmp = []
        for i in items:
                if i.startswith(d) and (i[len(d)+1:len(d)+9].isdecimal()):
                        tmp.append(i)

        for i in tmp:
                string = i
                ood = len(d) + 1
                doo = ood + len(now.strftime("%Y") + now.strftime("%m")+ now.strftime("%d"))
                data_pliku = strData(string[ood:doo])
                if do_daty > data_pliku:
                        print("DELETE: " + i  + " DATE: "+ str(data_pliku))
                        call = os.system("rm -r %s/%s" % (mount_point, i))
print("DONE")
