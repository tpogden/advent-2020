from operator import mul
from functools import reduce

# from math import gcd

import numpy as np

def read_times(fpath='data/13-demo.txt'):
    with open(fpath) as f:
        now = int(f.readline().strip())
        buses = [i for i in f.readline().strip().split(',')]
    return now, buses

def parse_buses(buses):
    buses_parsed = []
    bus_mods = []
    bus_idxs = []
    for i, b in enumerate(buses):
        if b is not 'x':
            buses_parsed.append(int(b))
            # bus_mods.append(int(b) - i)
            bus_idxs.append(i)
            bus_mods.append(int(b) - i%int(b))
    return buses_parsed, bus_mods, bus_idxs

# now, buses = read_times(fpath='data/13-demo.txt')
now, buses = read_times(fpath='data/13.txt')

# buses = [17, 'x', 13, 19]
# buses = [67,'x',7,59,61]
# buses = [67,7,'x',59,61]
# buses = [1789, 37, 47, 1889]

bp, bm, bi = parse_buses(buses)

print('bp:', bp)
print('bm:', bm)
print('bi:', bi)

def solve(bp, bi):
    n = 0
    step = 1
    for i, b in enumerate(bp):
        while (n + bi[i])%b != 0:
            n += step
        step *= b
    return n

print('sol:', solve(bp, bi))
