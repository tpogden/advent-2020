
def read_instruct(fpath='data/08-demo-b.txt'):
    with open(fpath) as f:
        arr = [l.strip().split(' ') for l in f.readlines()]
    return arr

def process_instruct(arr):
    acc = 0
    visited = set()
    i = 0
    normal = False
    while True:
        # print(visited)
        if i == len(arr):
            print('Terminated normally!')
            normal = True
            break
        if i in visited:
            print(f'{i} has been visited before!')
            break
        else:
            visited.add(i)
        if arr[i][0] == 'nop':
            i += 1
        elif arr[i][0] == 'acc':
            acc += int(arr[i][1])
            i += 1
        elif arr[i][0] == 'jmp':
            i += int(arr[i][1])
    # print(visited)
    # print(acc)
    # print(normal)
    return acc, normal

def swap_instruct(arr, i):
    if arr[i][0] == 'nop':
        arr[i][0] = 'jmp'
    elif arr[i][0] == 'jmp':
        arr[i][0] = 'nop'
    else: # 'acc'
        # pass
        return False
    return True #arr

def fix_instruct(arr):
    for i, a in enumerate(arr):
        print(i, a)
        swap_instruct(arr, i)
        # print(i, a)
        acc, normal = process_instruct(arr)
        if normal:
            print(acc, normal)
            print('Now normal!')
            return acc, normal
        else: # swap back
            swap_instruct(arr, i)
    return False

# arr = read_instruct(fpath='data/08-demo.txt')
# arr = read_instruct(fpath='data/08-demo-b.txt')
arr = read_instruct(fpath='data/08.txt')
# acc, normal = process_instruct(arr)
# print(acc, normal)

acc, _ = fix_instruct(arr)
print('sol:', acc)
