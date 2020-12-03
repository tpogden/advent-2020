from operator import mul
from functools import reduce

with open('data/03.txt') as f:
    arr = [l.strip() for l in f.readlines()]

n = len(arr)
m = len(arr[0])

step_list = [{'down': 1, 'right': 1}, {'down': 1, 'right': 3}, 
    {'down': 1, 'right': 5}, {'down': 1, 'right': 7}, {'down': 2, 'right': 1}]

tree_list = [0]*len(step_list)

for k, s in enumerate(step_list):
    for ii, i in enumerate(range(0, n, s['down'])):
        j = s['right']*ii
        if arr[i][j%m] == '#':
            tree_list[k] += 1

print(tree_list)

print('sol:', reduce(mul, tree_list, 1))


