import psutil
import datetime


def ileCPU():
    tmp0 = psutil.cpu_percent(interval=1, percpu=True)
    return str(tmp0)


CPU_NUM = psutil.cpu_count(logical=False)
CPU_CORE = psutil.cpu_count()
MEM = psutil.virtual_memory()
SWAP = psutil.swap_memory()
DISK = psutil.disk_usage('C:/')

MEM_total = round(MEM.total / (1024 ** 3), 2)
MEM_percent = MEM.percent
SWAP_usage = round(SWAP.used / (1024 ** 3), 2)
SWAP_available = round(SWAP.total / (1024 ** 3), 2)

DISK_C_total = round(DISK.total / (1024 ** 3), 2)
DISK_C_percent = DISK.percent

BOOT_TIME = datetime.datetime.fromtimestamp(
    psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

print("\tKacper")
print("Boot time: " + str(BOOT_TIME))
print("System CPU (physical/logical):  "+str(CPU_NUM)+"/"+str(CPU_CORE))
print("Usage CPU :" + ileCPU())

print("Total memory: " + str(MEM_total)
      + "GB and used: " + str(MEM_percent) + "%")
print("Used SWAP: " + str(SWAP_usage)
      + "GB of total: " + str(SWAP_available) + "GB")
print("Disk C: " + str(DISK_C_total)
      + "GB and used: "+str(DISK_C_percent) + "%")

input("Enter to exit\n")
