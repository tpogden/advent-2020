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

def rot_90(waypoint, left_or_right='L', n_rot_90=1):
    new_waypoint = waypoint
    for i in range(n_rot_90):
        new_waypoint *= Rotate[left_or_right].value
    return new_waypoint

def step(a, pos, waypoint):
    kind = a[0]
    val = a[1]
    if kind in ['E', 'N', 'W', 'S']:
        new_pos = pos
        new_waypoint = waypoint + Move[kind].value*val
    elif kind in ['F']:
        new_pos = pos + waypoint*val        
        new_waypoint = waypoint
    elif kind in ['L', 'R']:
        new_pos = pos
        new_waypoint = rot_90(waypoint=waypoint, left_or_right=kind, 
            n_rot_90=val//90)
    return new_pos, new_waypoint

def walk(arr):
    pos = 0 + 0j
    waypoint = 10 + 1j
    for a in arr:
        print(a)
        pos, waypoint = step(a, pos, waypoint)
    return pos, waypoint

# arr = read_arr(fpath='data/12-demo.txt')
arr = read_arr(fpath='data/12.txt')
pos, waypoint = walk(arr)
print('sol:', int(abs(pos.real) + abs(pos.imag)))
