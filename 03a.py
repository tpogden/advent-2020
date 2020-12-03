with open('data/03.txt') as f:
    arr = [l.strip() for l in f.readlines()]

n = len(arr)
m = len(arr[0])

trees = 0
for i in range(n):
    j = 3*i
    if arr[i][j%m] == '#':
        trees += 1

print('sol:', trees)
