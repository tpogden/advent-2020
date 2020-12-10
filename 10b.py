# from utils import Graph, BacktrackerGraphPaths
from functools import lru_cache

from collections import defaultdict

def read_arr(fpath='data/10-demo.txt'):
    with open(fpath) as f:
        arr = [int(l.strip()) for l in f.readlines()]
    return arr

# arr = read_arr()
# arr = read_arr(fpath='data/10-demo-b.txt')
arr = read_arr(fpath='data/10.txt')

arr.append(0)
arr.append(max(arr) + 3)
sarr = sorted(arr)

print(sarr)

edgedict_rev = defaultdict(list)

for i, s_i in enumerate(sarr):
    for j, s_j in enumerate(sarr[i+1:i+4]):
        if s_j - s_i <= 3:
            edgedict_rev[s_j].append(s_i)

print(edgedict_rev)

@lru_cache(maxsize=1000)
def num_ways_to(node):
    if node == 0:
        return 1
    else:
        n = 0
        for i in edgedict_rev[node]:
            n += num_ways_to(node=i)
    return n

goal = max(sarr)

n = num_ways_to(node=goal)

print('sol:', n)
