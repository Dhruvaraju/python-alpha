- [Dealing with Files folders and process](#dealing-with-files-folders-and-process)
  - [Installation and setting up ide](#installation-and-setting-up-ide)
  - [Getting details of modules](#getting-details-of-modules)
  - [Fetching disk related information](#fetching-disk-related-information)
  - [Fetching process related information](#fetching-process-related-information)
  - [Platform and environment variable information](#platform-and-environment-variable-information)

# Dealing with Files folders and process

- This explains how to deal with files, folders and processes using python.
- We need to use the modules `os, shutil, psutil`
- `os,shutil` are inbuilt modules provided by python.
- `psutil` need to be installed.

> All the requirements for this are mentioned in requirements.txt

## Installation and setting up ide

- Use microsoft visual studio code as ide
- Navigate to the folder you like to place code
- execute `python.exe -m venv .venv` to create a virtual environment.
- `.venv\Scripts\activate.bat` to activate virtual environment in current folder.
- `pip install -r requirements.txt` to install all dependencies or modules required.

## Getting details of modules

- mentioned in `python-modules.py`
- after importing a module use the dir function provided by os module to log all the functions present in a module.
- Example: `print(dir(os))` to print details of os module.
- Others are added in `python-modules.py`

## Fetching disk related information

- Using `psutil` we can fetch disk related info
- `pprint(psutil.disk_partitions())` to get disk partition related information.
- `pprint(psutil.disk_usage('/'))` to get disk usage information
- `pprint(psutil.disk_io_counters(perdisk=True))` to get disk IO related information

## Fetching process related information

- process related information can be found from `psutil.process_iter()`
- To print all processes names and corresponding process ids.

```python
for process in psutil.process_iter():
    try:
        process_name = process.name()
        process_id = process.pid
        print(process_name, ":::", process_id)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
```

## Platform and environment variable information
- 