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

def look(look_arr):
    for a in look_arr:
        if a == 'L' or a == '#':
            return a 
    return '.'

def look_right(i, j, arr):
    rarr = arr[i][j+1:]
    return look(rarr)

def look_left(i, j, arr):
    larr = list(reversed(arr[i][:j]))
    return look(larr)

def look_up(i, j, arr):
    uarr = []
    for ui in range(i-1, 0, -1):
        uarr.append(arr[ui][j])
    return look(uarr)

def look_down(i, j, arr):
    darr = []
    for di in range(i+1, len(arr)):
        darr.append(arr[di][j])
    return look(darr)

def look_upright(i, j, arr):
    larr = []
    num_up = i-1
    num_right = len(arr[0]) - (j+1)
    li = i-1
    lj = j+1
    for k in range(min(num_up, num_right)):
        larr.append(arr[li][lj])
        li -= 1
        lj += 1
    return look(larr)

def look_downright(i, j, arr):
    larr = []
    num_down = len(arr) - (i+1)
    num_right = len(arr[0]) - (j+1)
    li = i+1
    lj = j+1
    for k in range(min(num_down, num_right)):
        larr.append(arr[li][lj])
        li += 1
        lj += 1
    return look(larr)

def look_upleft(i, j, arr):
    larr = []
    num_up = i-1
    num_left = j-1
    li = i-1
    lj = j-1
    for k in range(min(num_up, num_left)):
        larr.append(arr[li][lj])
        li -= 1
        lj -= 1
    return look(larr)

def look_downleft(i, j, arr):
    larr = []
    num_down = len(arr) - (i+1)
    num_left = j-1
    li = i+1
    lj = j-1
    for k in range(min(num_down, num_left)):
        larr.append(arr[li][lj])
        li += 1
        lj -= 1
    return look(larr)

def look_num(i, j, arr):
    lu = look_upleft(i, j, arr) == '#'
    l = look_left(i, j, arr) == '#'
    ld = look_downleft(i, j, arr) == '#'
    u = look_up(i, j, arr) == '#'
    d = look_down(i, j, arr) == '#'
    ru = look_upright(i, j, arr) == '#'
    r = look_right(i, j, arr) == '#'
    rd = look_downright(i, j, arr) == '#'
    return lu + l + ld + u + d + ru + r + rd

def step(i, j, arr):
    n_adj = look_num(i, j, arr)
    if arr[i][j] == 'L' and n_adj == 0: # empty
        return '#', 1, n_adj
    if arr[i][j] == '#' and n_adj > 4: # occupied
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

# arr = read_arr(fpath='data/11-demo.txt')
arr = read_arr(fpath='data/11.txt')
arr = pad_arr(arr)
# print(arr)
# print(np.array(arr))

num_occupied, num_changed, steps = step_til_stable(arr)

print('sol:', num_occupied)
