from enum import Enum

class Move(Enum):
    E = 1 + 0j
    N = 0 + 1j
    W = -1 + 0j
    S = 0 - 1j

class Rotate(Enum):
    L = 1j
    R = -1j

def read_arr(fpath='data/12-demo.txt'):
    with open(fpath) as f:
        arr = [[l[0], int(l[1:].strip())] for l in f.readlines()]
    return arr

def rot_90(dir, left_or_right='L', n_rot_90=1):
    newdir = dir
    for i in range(n_rot_90):
        newdir *= Rotate[left_or_right].value
    return newdir

def step(a, pos, dir):
    kind = a[0]
    val = a[1]
    if kind in ['E', 'N', 'W', 'S']:
        new_pos = pos + Move[kind].value*val
        new_dir = dir
    elif kind in ['F']:
        new_pos = pos + dir*val
        new_dir = dir
    elif kind in ['L', 'R']:
        new_pos = pos
        new_dir = rot_90(dir=dir, left_or_right=kind, n_rot_90=val//90)
    return new_pos, new_dir

def walk(arr):
    pos = 0 + 0j
    dir = Move.E.value
    for a in arr:
        pos, dir = step(a, pos, dir)
    return pos, dir

# arr = read_arr(fpath='data/12-demo.txt')
arr = read_arr(fpath='data/12.txt')
pos, dir = walk(arr)
print('sol:', int(abs(pos.real) + abs(pos.imag)))
