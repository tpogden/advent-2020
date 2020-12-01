from utils import bs

with open('data/01.txt') as f:
    arr = [int(l.strip()) for l in f.readlines()]
    
sarr = sorted(arr)

target = 2020

m = len(sarr)//2
for i in sarr[:m]:
    j = target - i
    if bs(sarr[m:], j):
        print(i, j, i + j, i*j)
        sol = i*j

print('sol:', sol)