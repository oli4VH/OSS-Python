#!/usr/bin/python3
import time

def get_loadavg():
    with open('/proc/loadavg', 'r') as f:
        loadavg = f.read().strip().split()
    return loadavg[:3]

prev_loadavg = get_loadavg()

while True:
    loadavg = get_loadavg()
    if loadavg != prev_loadavg:
        print(f'Loadavg changed: {prev_loadavg} -> {loadavg}')
        prev_loadavg = loadavg

    if float(loadavg[0]) > 0.6 or float(loadavg[0]) > 1.0:
        print(f'Loadavg of last minute is high ({loadavg[0]}), sleeping for 30 seconds...')
        time.sleep(30)
    else:
        time.sleep(1)
