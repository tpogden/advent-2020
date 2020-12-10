def read_arr(fpath='data/10-demo.txt'):
    with open(fpath) as f:
        arr = [int(l.strip()) for l in f.readlines()]
    return arr

# arr = read_arr()
arr = read_arr(fpath='data/10.txt')

arr.append(0)
arr.append(max(arr) + 3)
sarr = sorted(arr)

print(sarr)

diffs = [sarr[i] - sarr[i-1] for i, _ in enumerate(sarr[1:], start=1)]

print(diffs)

dc = {a: diffs.count(a) for a in [1,2,3]}

print(dc)

sol = dc[1]*dc[3]

print('sol:', sol)
