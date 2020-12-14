from itertools import product

def read_arr(fpath='data/14-demo.txt'):
    with open(fpath) as f:
        arr = [l.strip().split(' = ') for l in f.readlines()]
    return arr

def read_memval(a):
    mem = int(a[0].strip('mem[').strip(']'))
    val = int(a[1])
    return mem, val

def int_to_bitlist(n):
    bl = list('{0:b}'.format(n).zfill(36))
    return bl

def apply_mask_to_bitlist(bitlist, mask):
    new_bitlist = bitlist[:]
    mask_list = list(mask)
    for i, b_i in enumerate(new_bitlist):
        if mask[i] == '1':
            new_bitlist[i] = '1'
        elif mask[i] == 'X':
            new_bitlist[i] = 'X'
        elif mask[i] == '0':
            pass
    return new_bitlist

def mem_list(floating_bitlist):
    start_m = list(floating_bitlist)
    pos_X = [i for i, m in enumerate(start_m) if m is 'X']
    # print(pos_X)
    ml = []
    prod = list(product(['0', '1'], repeat=len(pos_X)))
    # print('prod:', prod)
    for p in prod:
        new_m = start_m[:]
        # print('p:', p)
        for i, p_i in enumerate(p):
            new_m[pos_X[i]] = p_i
        ml.append(new_m)
    return ml

def mem_list_to_dec(mem_list):
    return [int(''.join(m), 2) for m in mem_list] 

def run_program(arr):
    memory = dict()
    mask = None
    mem = None
    val = None
    for a in arr:
        if a[0] == 'mask':
            mask = a[1]
            print('mask:', mask)
        else:
            mem, val = read_memval(a)
            print('mem:', mem, 'val:', val)
            bl = int_to_bitlist(mem)
            new_bl = apply_mask_to_bitlist(bl, mask)
            ml = mem_list(floating_bitlist=new_bl)
            mld = mem_list_to_dec(mem_list=ml)
            # print('mld:', mld)
            for m in mld:
                memory[m] = val
    return memory

# arr = read_arr(fpath='data/14-demo-b.txt')
arr = read_arr(fpath='data/14.txt')
memory = run_program(arr)
print('sol:', sum(memory.values()))
