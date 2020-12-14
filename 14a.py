def read_arr(fpath='data/14-demo.txt'):
    with open(fpath) as f:
        arr = [l.strip().split(' = ') for l in f.readlines()]
    return arr

def read_memval(a):
    mem = int(a[0].strip('mem[').strip(']'))
    val = int(a[1])
    return mem, val

def mask_dict(mask):
    return {i: m for i, m in enumerate(mask) if m is not 'X'}

def int_to_bitlist(n):
    bl = list('{0:b}'.format(n).zfill(36))
    return bl

def apply_mask_to_val(n, mask):
    bl = int_to_bitlist(n)
    md = mask_dict(mask)
    for i in md:
        bl[i] = md[i]
    return int(''.join(bl), 2)
    
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
            newval = apply_mask_to_val(val, mask)
            print('newval:', newval)
            memory[mem] = newval
    return memory

# arr = read_arr(fpath='data/14-demo.txt')
arr = read_arr(fpath='data/14.txt')
memory = run_program(arr)
print('sol:', sum(memory.values()))
