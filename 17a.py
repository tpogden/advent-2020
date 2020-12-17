import numpy as np

def read_arr(fpath='data/17-demo.txt'):
    with open(fpath) as f:
        arr = [list(l.strip().replace('.', '0').replace('#', '1')) 
            for l in f.readlines()]
        arr = [[int(i) for i in a] for a in arr]
    return arr

arr = read_arr(fpath='data/17-demo.txt')

def init_cubes(arr, num_cycles=1):

    start = np.array(arr)
    print(start)

    start_dim = len(arr)
    dim = start_dim + 2*num_cycles
    idx_0 = num_cycles

    print('start_dim:', start_dim, 'num_cycles:', num_cycles, 'dim:', dim)

    cubes = np.zeros(shape=(num_cycles+1, dim, dim, dim))
    cubes[0, 0, idx_0:idx_0+start_dim, idx_0:idx_0+start_dim] = start
    print(cubes)
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

    # print(idx)
    # region = cubes[0]
    region = cubes[cycle, c_x_min:c_x_max, c_y_min:c_y_max, c_z_min:c_z_max]
    print(region)
    return np.sum(region) - cubes[cycle, idx[0], idx[1], idx[2]]

cubes = init_cubes(arr, num_cycles=1)

sum_n = sum_neighbors(cubes, cycle=0, idx=(0,1,1))

print(sum_n)
