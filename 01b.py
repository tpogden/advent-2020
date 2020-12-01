from utils import bs

with open('data/01.txt') as f:
    arr = [int(l.strip()) for l in f.readlines()]

sarr = sorted(arr)

pairdict = {(s_i, s_j): s_i + s_j 
    for i, s_i in enumerate(sarr) 
    for j, s_j in enumerate(sarr[i+1:])}

target = 2020

for p, ps in pairdict.items():
    target_k = target - ps
    if bs(sarr, target_k):
        print(p, ps, target_k, p[0]*p[1]*target_k)
        sol = p[0]*p[1]*target_k

print('sol:', sol)
