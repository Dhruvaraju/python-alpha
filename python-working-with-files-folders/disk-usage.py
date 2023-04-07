import psutil
from pprint import pprint

# To get partition level information
pprint(psutil.disk_partitions())
print("----\n")

# To print disk usage 
pprint(psutil.disk_usage('/'))
print("----\n")


# Disk io counters 
pprint(psutil.disk_io_counters(perdisk=False, nowrap=True))
pprint(psutil.disk_io_counters(perdisk=True))
print("----\n")
