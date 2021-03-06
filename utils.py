from collections import defaultdict, deque

def bs(arr, val, lo=0, hi=None):
    """Binary search for val in arr."""
    if hi is None:
        hi = len(arr)
    if lo >= hi:
        return None
    m = (hi+lo)//2
    if arr[m] == val:
        return m
    if arr[m] > val:
        return bs(arr, val, lo=0, hi=m)
    else:
        return bs(arr, val, lo=m+1, hi=hi)


class Graph:

    def __init__(self, directed=False, edgelist=None):
        self.g = defaultdict(set)
        self.directed = directed
        self.weights = defaultdict(lambda: int(0))
        if edgelist:
            self.insert_edgelist(edgelist)

    def __repr__(self):
        return self.dot_repr()

    def dot_repr(self):
        '''Return DOT languange string representation of the graph.'''
        slist = []
        if self.directed:
            slist.append('digraph {')
            for x, y in self.edgelist():
                slist.append(f'  "{x}" -> "{y}" [label="{self.weights[(x, y)]}"]')
        else:
            slist.append('graph {')
            for x, y in self.edgelist():
                if x <= y:
                    slist.append(f'  "{x}" -- "{y}" [label="{self.weights[(x, y)]}"]')
        slist.append('}')
        return '\n'.join(slist)

    def insert_edge(self, x, y, weight=None):
        self.g[x].add(y)
        if weight:
            self.weights[(x, y)] = weight
        if not self.directed:
            self.g[y].add(x)
            if weight:
                self.weights[(y, x)] = weight

    def insert_edgelist(self, edgelist):
        for e in edgelist:
            self.insert_edge(*e)

    def edgelist(self):
        return [(v, e) for v in self.g for e in self.g[v]]

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                stack.extend(self.g[v] - visited)
        return visited

    def bfs(self, start):
        visited, queue = set(), deque([start])
        while queue:
            v = queue.popleft()
            if v not in visited:
                visited.add(v)
                queue.extend(self.g[v] - visited)
        return visited

    def bfs_paths(self, start, goal):
        '''Generates paths from start vertex to goal vertex.

        Because it uses breadth-first traversal, the first path yielded is 
        guaranteed to be the shortest possible (see shortest_path()).

        Args:
            start: start vertex
            goal: goal vertex 

        Yields:
            paths from start to goal
        '''
        queue = deque([(start, [start])])
        while queue:
            (v, path) = queue.popleft()
            for nextv in self.g[v] - set(path):
                if nextv == goal:
                    yield path + [nextv]
                else:
                    queue.append((nextv, path + [nextv]))

    def shortest_path(self, start, goal):
        path_gen = bfs_paths(start, goal)
        return next(path_gen)

    def dfs_paths(self, start, goal):
        '''Generates paths from start vertex to goal vertex using depth-first
        search.
        
        Notes:
            Because start is kept out of the path (compare with bfs_paths) here
            it can be used to find cycles. See dfs_cycles().
        '''
        stack = [(start, [])]
        while stack:
            v, path = stack.pop()
            for nextv in self.g[v] - set(path):
                if nextv == goal:
                    yield [start] + path + [nextv]
                else:
                    stack.append((nextv, path + [nextv]))

    def dfs_cycles(self, start):
        return self.dfs_paths(start=start, goal=start)

    def is_dag(self):
        '''Returns True if the graph is directed acyclic graph.'''
        '''TODO: can do faster with topo_sort.'''
        for v in list(self.g.keys()):
            if list(self.dfs_cycles(v)):
                return False
        return True


class Backtracker:

    def __init__(self):
        self.finished = False
        self.sols = []

    def solve(self, A=None):
        self.sols = []
        if A is None:
            A = []
        self.backtrack(A=A)
        return self.sols

    def backtrack(self, A):
        if self.is_sol(A):
            self.process_sol(A)
        else:
            for c in self.candidates(A):
                self.make_move(A, c)
                self.backtrack(A)
                self.unmake_move(A, c)
                if self.finished:
                    return None

    def is_sol(self, A):
        raise NotImplementedError

    def candidates(self, A):
        raise NotImplementedError

    def process_sol(self, A):
        self.sols.append(A[:])

    def make_move(self, A, c):
        A.append(c)

    def unmake_move(self, A, c):
        A.pop()

class BacktrackerGraphPaths(Backtracker):

    def __init__(self, graph):
        super().__init__()
        self.graph = graph

    def solve(self, start, goal):
        self.goal = goal
        return super().solve(A=[start])
    
    def process_sol(self, A):
        self.sols.append(A[:])

    # def solve(self, start, goal, A=None):
    #     self.sols = 0
    #     self.goal = goal
    #     if A is None:
    #         A = []
    #     self.backtrack(A=A)
    #     return self.sols

    # def process_sol(self, A):
    #     self.sols += 1

    def is_sol(self, A):
        return A[-1] == self.goal

    def candidates(self, A):
        return self.graph.g[A[-1]] - set(A)

