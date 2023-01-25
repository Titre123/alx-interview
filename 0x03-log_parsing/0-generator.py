#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

with open('./xt.txt', 'r') as f:
    fs = f.readlines()
    for line in fs:
        sys.stdout.write(line)
