def read_arr(fpath='data/09-demo.txt'):
    with open(fpath) as f:
        arr = [int(l.strip()) for l in f.readlines()]
    return arr

def get_prev_n(arr, i, n):
    return arr[i-n:i]

def prev_n_sums(arr, i, n):
    prev_n = get_prev_n(arr, i, n)
    # print('prev_n:', prev_n)
    # s = set()
    s = set()
    for i in range(n):
        for j in range(i+1, n):
            # print(i, j)
            # print(prev_n[i], prev_n[j], prev_n[i] + prev_n[j])
            s.add(prev_n[i] + prev_n[j])
    return s

def find_invalid_val(arr, n):

    for i in range(n, len(arr)+1):
    # for i in range(n, n+1):
        # print(i)
        # prev_n = get_prev_n(arr, i, n)
        # print(prev_n)
        s = prev_n_sums(arr=arr, i=i, n=n)
        # print(s)
        if arr[i] in s:
            pass
            # print(i, arr[i], 'valid!')
        else:
            print(i, arr[i], 'INVALID!')
            return arr[i]

def contiguous_sums(arr, target):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            cs = sum(arr[i:j+1])
            if cs == target:
                return cs, min(arr[i:j+1]), max(arr[i:j+1])
                # return cs, arr[i], arr[j+1]
    return None

# arr = read_arr()
# n = 5

arr = read_arr(fpath='data/09.txt')
n = 25

print(arr)

invalid_val = find_invalid_val(arr=arr, n=n)
print('invalid_val:', invalid_val)

cs, minv, maxv = contiguous_sums(arr, invalid_val)
print(cs, minv, maxv)
sol = maxv + minv
print('sol:', sol)

