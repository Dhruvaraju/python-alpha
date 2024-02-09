import psutil
from pprint import pprint

# For fetching list of processes:
pprint(psutil.process_iter())
print("---\n")

# Intreating through all the processes and printing details

for process in psutil.process_iter():
    try:
        process_name = process.name()
        process_id = process.pid
        print(process_name, ":::", process_id)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Iterate through all processes and gather required details
all_processes = list()
for process in psutil.process_iter():
    try:
        all_processes.append(process.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']))
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

pprint(all_processes)