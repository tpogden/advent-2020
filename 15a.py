
def read_arr(fpath='data/15-demo.txt'):
    with open(fpath) as f:
        arr = [int(i) for i in f.readline().strip().split(',')]
    return arr

# arr = read_arr(fpath='data/15-demo.txt')
arr = read_arr(fpath='data/15.txt')

# arr = [1,3,2]
# arr = [1,2,3]
# print(arr)


def play(start_arr, n=2020):
    prev_dict = {a_i:i+1 for i, a_i in enumerate(start_arr[:-1])}
    next_val = start_arr[-1]
    for i in range(len(start_arr), n+1):
        spoken = next_val
        # print('i:', i, 'spoken:', spoken)
        # print('prev_dict:', prev_dict)       
        if spoken in prev_dict:
            # print('spoken:', spoken, 'is already in prev_dict')
            diff = i - prev_dict[spoken]
            # print('diff:', diff)
            next_val = diff
        else:
            # print('spoken:', spoken, 'is NOT already in prev_dict')
            next_val = 0
        prev_dict[spoken] = i
    return spoken
    
sol = play(start_arr=arr, n=2020)

print('sol:', sol)
