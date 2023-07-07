#!/usr/bin/python
import os
from pathlib import Path
import subprocess, json
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

output = subprocess.run(
    ['vnstat','-i','wlan0','--json','d','--limit','1'],
    capture_output=True,
    text=True,
    check=True
)

output_dict = json.loads(output.stdout)
dataUsage = convert_size(int(output_dict["interfaces"][0]['traffic']['day'][0]['rx']))
print(dataUsage)

