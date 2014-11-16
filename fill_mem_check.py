#!/usr/bin/env python 
"""
check the free memmory available on the machine 
usage: fill_mem_check.py <number-of-gigabytes>
"""

import sys 
import time 

if len(sys.argv) != 2:
    print __doc__
    sys.exit()

count = int(sys.argv[1])
gigabyte = (0,) * (1024 * 1024 * 1024 / 8) #Each element is allocated as double, which means 8 byte for each element

data = gigabyte * count 

while True:
    print "getting %d GB memory for use" % count  
    time.sleep(1)
