import numpy as np

np.set_printoptions(threshold=100000)

def read_arr(fpath='data/17-demo.txt'):
    with open(fpath) as f:
        arr = [list(l.strip().replace('.', '0').replace('#', '1')) 
            for l in f.readlines()]
        arr = [[int(i) for i in a] for a in arr]
    return arr

def init_cubes(arr, num_cycles=1):

    start = np.array(arr)
    print(start)

    start_dim = len(arr)
    dim = start_dim + 2*num_cycles
    idx_0 = num_cycles

    print('start_dim:', start_dim, 'num_cycles:', num_cycles, 'dim:', dim)

    cubes = np.zeros(shape=(num_cycles+1, dim, dim, dim), dtype=np.int)
    cubes[0, dim//2, idx_0:idx_0+start_dim, idx_0:idx_0+start_dim] = start
    # print(cubes)
    return cubes

def sum_neighbors(cubes, cycle=0, idx=(0,0,0)):
    if idx[0] > 0:
        c_x_min = idx[0]-1
    else:
        c_x_min = 0
    if idx[1] > 0:
        c_y_min = idx[1]-1
    else:
        c_y_min = 0
    if idx[2] > 0:
        c_z_min = idx[2]-1
    else:
        c_z_min = 0
    if idx[0] < cubes.shape[1]:
        c_x_max = idx[0] + 2
    else:
        c_x_max = cubes.shape[1]
    if idx[1] < cubes.shape[2]:
        c_y_max = idx[1] + 2
    else:
        c_y_max = cubes.shape[2]
    if idx[2] < cubes.shape[3]:
        c_z_max = idx[2] + 2
    else:
        c_z_max = cubes.shape[3]

    region = cubes[cycle, c_x_min:c_x_max, c_y_min:c_y_max, c_z_min:c_z_max]
    # print(region)
    # print(region.shape)
    return np.sum(region) - cubes[cycle, idx[0], idx[1], idx[2]]

def sum_neighbors_all(cubes, cycle=0):
    sna = np.zeros(cubes[cycle].shape)
    for x in range(cubes[cycle].shape[0]):
        for y in range(cubes[cycle].shape[1]):
            for z in range(cubes[cycle].shape[0]):
                sna[x, y, z] = sum_neighbors(cubes, cycle, idx=(x,y,z))
    return sna

def next_is_active(cubes, cycle=0):
    sna = sum_neighbors_all(cubes, cycle)
    # print('sna:\n', sna)
    rule_1 = np.logical_and(cubes[cycle], 
        np.logical_or(sna == 2, sna == 3)).astype(int)
    # print('rule_1:\n', rule_1)
    rule_2 = np.logical_and(np.logical_not(cubes[cycle]), sna == 3).astype(int)
    # print('rule_2:\n', rule_2)
    # at max, one of rule_1 and rule_2 can be true, so we can sum them
    return rule_1 + rule_2

def step_cubes(cubes, cycle=0):
    sna = sum_neighbors_all(cubes, cycle=cycle)
    cubes[cycle+1] = next_is_active(cubes, cycle=cycle)
    return cubes

def get_num_active(cubes):
    return np.sum(cubes, axis=(1,2,3))

def walk_cubes(cubes, num_cycles):
    for cycle in range(num_cycles):
        step_cubes(cubes, cycle=cycle)
    return cubes

# arr = read_arr(fpath='data/17-demo.txt')
arr = read_arr(fpath='data/17.txt')

NUM_CYCLES = 6

cubes = init_cubes(arr, num_cycles=NUM_CYCLES)
walk_cubes(cubes=cubes, num_cycles=NUM_CYCLES)

num_active = get_num_active(cubes)
print('num_active:', num_active)

print('sol:', num_active[-1])
