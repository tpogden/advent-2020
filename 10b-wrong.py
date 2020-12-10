# Don't try to use this for the final input data!

from utils import Graph, BacktrackerGraphPaths

def read_arr(fpath='data/10-demo.txt'):
    with open(fpath) as f:
        arr = [int(l.strip()) for l in f.readlines()]
    return arr

# arr = read_arr()
arr = read_arr(fpath='data/10-demo-b.txt')
# arr = read_arr(fpath='data/10.txt')

arr.append(0)
arr.append(max(arr) + 3)
sarr = sorted(arr)

print(sarr)

edges = []
for i, s_i in enumerate(sarr):
    for j, s_j in enumerate(sarr[i+1:i+4]):
        if s_j - s_i <= 3:
            edges.append((s_i, s_j))
print(edges)

g = Graph(directed=True, edgelist=edges)

print(g)

start = min(sarr)
goal = max(sarr)

b = BacktrackerGraphPaths(graph=g)

paths = b.solve(start=start, goal=goal)
sol = len(paths)

print('sol:', sol)
