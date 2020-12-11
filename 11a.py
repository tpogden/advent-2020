# import numpy as np # just for visualising arrays

def read_arr(fpath='data/11-demo.txt'):
    with open(fpath) as f:
        arr = [list(l.strip()) for l in f.readlines()]
    return arr

def pad_arr(arr):
    for a in arr:
        a.insert(0, '0')
        a.append('0')
    pad_top = ['0']*len(arr[0]) 
    arr.insert(0, pad_top[:])
    arr.append(pad_top[:])
    return arr[:]

def num_occupied(arr):
    n = 0
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] == '#':
                n += 1
    return n

def num_adj(i, j, arr):
    lu = arr[i-1][j-1] == '#'
    l = arr[i][j-1] == '#'
    ld = arr[i+1][j-1] == '#'
    u = arr[i-1][j] == '#'
    d = arr[i+1][j] == '#'
    ru = arr[i-1][j+1] == '#'
    r = arr[i][j+1] == '#'
    rd = arr[i+1][j+1] == '#'
    return lu + l + ld + u + d + ru + r + rd

def adj_all(arr):
    adj = [[0 for i in arr] for j in arr[0]]
    for i, a_i in enumerate(arr[1:-1], start=1):
        for j, a_j in enumerate(a_i[1:-1], start=1):
            adj[i][j] = num_adj(i=i, j=j, arr=arr)
    return adj

def step(i, j, arr):
    n_adj = num_adj(i, j, arr)
    if arr[i][j] == 'L' and n_adj == 0: # empty
        return '#', 1, n_adj
    if arr[i][j] == '#' and n_adj > 3: # occupied
        return 'L', 1, n_adj
    return arr[i][j], 0, n_adj

def step_all(arr):
    new_arr =  [['0' for j in arr[0]] for i in arr]
    num_changed = 0
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            old_a = arr[i][j]
            new_a, changed, n_adj = step(i, j, arr)
            # print('i:', i, 'j:', j, 'n_adj:', n_adj, 'old_a:', old_a, 'new_a:', new_a, 'changed:', changed)
            new_arr[i][j] = new_a
            num_changed += changed
    return new_arr, num_changed

def step_til_stable(arr):
    num_changed = -1
    steps = 0 
    while num_changed != 0:
        arr, num_changed = step_all(arr)
        steps += 1
        print('steps:', steps)
        print('num_occupied:', num_occupied(arr))
        print('num_changed:', num_changed)
    return num_occupied(arr), num_changed, steps

arr = read_arr(fpath='data/11.txt')
arr = pad_arr(arr)

num_occupied, num_changed, steps = step_til_stable(arr)

print('sol:', num_occupied)
