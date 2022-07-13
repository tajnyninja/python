#!/usr/bin/python3

import os
import datetime

# mount check
print ("mount test:")
share_host = ("10.0.0.61")
share_point = ("/ifs/backup/wiki")
mount_point = ("/mnt/backup")
check_mount = (share_host + ":" + share_point + " on " + mount_point)
item = ("wikijs")
type = ("dump")

#call = os.system("mount | grep \"%s:%s on %s\"" % (share_host, share_point, mount_point))
call = os.system("ls /mnt/backup/_MOUNTED_ ")
print(call)

if not call:
        print("mount is OK")
else:
        print("not mounted!")

# date
d = datetime.datetime.now()
print(d.strftime("%Y") + d.strftime("%m")+ d.strftime("%d"))
#print(str(d.year) + str(d.day))

#make dump
call = os.system("echo mysqldump -u wikijs --password=Aq1ki8gt -h 127.0.0.1 %s \> %s/%s_%s.%s" % (item, mount_point, item, (d.strftime("%Y") + d.strftime("%m")+ d.strftime("%d")) ,type))

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
print(items)
