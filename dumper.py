#!/usr/bin/python3

import os
import sys
import datetime

# vars
print ("mount test:")
mounted = true
share_host = ("10.0.0.61")
share_point = ("/ifs/backup/wiki")
mount_point = ("/mnt/backup")
check_mount = (share_host + ":" + share_point + " on " + mount_point)
item = ("wikijs")
type = ("dump")
ret = 30

# check mount - file in share
#call = os.system("mount | grep \"%s:%s on %s\"" % (share_host, share_point, mount_point))
call = os.system("ls  %s/_MOUNTED_" % (mount_point))
mounted = bool(call)

if not mounted:
       print("mount is OK")
else:
       print("not mounted!")
       sys.exit(1)

# date
d = datetime.datetime.now()
date = d.strftime("%Y") + d.strftime("%m")+ d.strftime("%d")
#print(str(d.year) + str(d.day))

#make dump
call = os.system("mysqldump -u wikijs --password=secret -h 127.0.0.1 %s > %s/%s_%s.%s" % (item, mount_point, item, (d.strftime("%Y") + d.strftime("%m")+ d.strftime("%d")) ,type))

# dump list
tmp = []

for path in os.listdir(mount_point):
       if os.path.isfile(os.path.join(mount_point, path)):
        tmp.append(path)

items = []
# prefix
for i in tmp:
       if i.startswith((item)):
        items.append(i)

# end
tmp = items
items = []
for i in tmp:
        if i.endswith((type)):
                items.append(i)


items.sort()

def strData(t0):
       tY = int(t0[0:4])
       tM = int(t0[4:6])
       tD = int(t0[6:8])
       d0 =  datetime.date(tY, tM, tD)
       return d0

def ileDni(d0, t0):
       d1 = d0 - datetime.timedelta(days = t0)
       return d1

teraz = strData(date)
do_daty = ileDni(teraz, ret)

for i in items:
       string = i
       ood = len(item) + 1
       doo = ood + len(date)
       data_pliku = strData((string[ood:doo]))
       if do_daty > data_pliku:
        print("DELETE: " + i  + " DATE: "+ str(data_pliku))
        call = os.system("rm %s/%s" % (mount_point, i))

print("DONE")
