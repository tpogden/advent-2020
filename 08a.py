
def read_instruct(fpath='data/08.txt'):
    with open(fpath) as f:
        arr = [l.strip().split(' ') for l in f.readlines()]
    return arr
    
arr = read_instruct()

def process_instruct(arr):
    acc = 0
    visited = set()
    i = 0
    while True:
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
    print(visited)
    print(acc)
    return acc

acc = process_instruct(arr)

print('sol:', acc)
