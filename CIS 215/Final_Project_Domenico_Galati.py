#Import
import sys
import os
import psutil
import time

def __init__(self):
    print()

def printBar(remainder, total):
    print('[' , end ='')
    while total>=0:
        if remainder >= 0:
            print(u"\u2588", end ="")
            remainder = remainder -1
        else:
            print('_', end ="")
        total = total-1
    print(']')

def memUsage():
    print("Memory:")
    memory = psutil.virtual_memory()
    print("Total:", round((memory.total)/ (2**30), 2), "GB")
    print("Used: ", memory.percent, end =" % \t ")
    printBar(memory.percent/3.5, 28.57)
    print("\n")

def storageUsage():
    print("Storage:")
    SSD = psutil.disk_usage('/mnt/meta')
    print ("Total: " +str(round(SSD.total / (2**30),2)), "GB")
    print ("Free:\t" +str(round(SSD.free / (2**30),2)), end =" GB ")
    remainder = SSD.free/ (2**32.85)
    total = SSD.total/ (2**32.85)
    printBar(remainder, total)
    print ("Used:\t " +str(round(SSD.percent,2)), end =" %   ")
    printBar(SSD.percent/3.5, 28.57)
    print("\n")

def cpuUsage():
    print("CPU:")
    CPU = psutil.cpu_count()
    print("Cores: ", CPU)
    CPU = psutil.cpu_percent(.5)
    print("Usage: ", CPU, "%", end="    ")
    printBar(CPU/3.5, 28.57)
    print("\n")

def networkUsage():
    print("Network:")
    network = psutil.net_if_stats()
    for type in network:
        try: #Can be finalized later and try/except can be removed
            if type == 'eno1.10' or type == 'eno1.20':
                print('Interface:',type)
                print("Enabled:  ",network[type].isup)
                print("Speed:\t  ", network[type].speed, "Mb\n")
        except NameError:
            print("Missing 1 or both interfaces")
            break
    network = psutil.net_io_counters() #Maybe useful for data rates?
    print("\n")

def apUsage():
    data = open( '/tmp/snowflake-last-telemetry-for-dom')
    temp = True
    nums = ''
    stats = ''
    for tup in data:
        if temp == True:
            nums = tup
        else:
            stats = tup
        temp = False
    nums = nums.strip("{")
    nums = nums.strip(" ")
    nums = nums.split(',')
    print("AP Info:")
    for point in nums:
        key, pair = point.split(':')
        print(key, end =":")
        print(pair)
    stats = stats.strip("{")
    stats = stats.strip(" ")
    stats = stats.split(',')
    for point in nums:
        key, pair = point.split(':')
        print(key, end =":")
        print(pair)

def main():
    cpuUsage()
    memUsage()
    storageUsage()
    networkUsage()
    apUsage()

if __name__ == "__main__":
    main()
    
