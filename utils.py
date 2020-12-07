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
                slist.append(f'  {x} -> {y}')
        else:
            slist.append('graph {')
            for x, y in self.edgelist():
                if x <= y:
                    slist.append(f'  {x} -- {y}')
        slist.append('}')
        return '\n'.join(slist)

    def insert_edge(self, x, y):
        self.g[x].add(y)
        if not self.directed:
            self.g[y].add(x)

    def insert_edgelist(self, edgelist):
        # TODO: rename insert_edges
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


# class GraphWeighted:

#     def __init__(self, directed=False, edgelist=None):
#         self.g = defaultdict(set)
#         self.directed = directed
#         if edgelist:
#             self.insert_edgelist(edgelist)

#     def __repr__(self):
#         return self.dot_repr()

#     def dot_repr(self):
#         '''Return DOT languange string representation of the graph.'''
#         slist = []
#         if self.directed:
#             slist.append('digraph {')
#             for x, y in self.edgelist():
#                 slist.append(f'  {x} -> {y[0]} [weight="{y[1]}"]')
#         else:
#             slist.append('graph {')
#             for x, y in self.edgelist():
#                 if x <= y:
#                     slist.append(f'  {x} -- {y[0]} weight="{y[1]}"]')
#         slist.append('}')
#         return '\n'.join(slist)

#     def insert_edge(self, x, y, weight):
#         self.g[x].add((y, weight))
#         if not self.directed:
#             self.g[y].add((x, weight))

#     def insert_edgelist(self, edgelist):
#         # TODO: rename insert_edges
#         for e in edgelist:
#             self.insert_edge(*e)

#     def edgelist(self):
#         return [(v, e) for v in self.g for e in self.g[v]]


#     def bfs(self, start):
#         visited, queue = set(), deque([start])
#         while queue:
#             v = queue.popleft()
#             if v not in visited:
#                 visited.add(v)
#                 for nextv in self.g[v]: #- visited:
#                     if nextv[0] not in visited:
#                         queue.append(nextv[0])
#         return visited

#     def bfs_paths(self, start, goal):
#         '''Generates paths from start vertex to goal vertex.

#         Because it uses breadth-first traversal, the first path yielded is 
#         guaranteed to be the shortest possible (see shortest_path()).

#         Args:
#             start: start vertex
#             goal: goal vertex 

#         Yields:
#             paths from start to goal
#         '''
#         queue = deque([(start, [start])])
#         while queue:
#             (v, path) = queue.popleft()
#             for nextv in self.g[v] - set(path):
#                 if nextv == goal:
#                     yield path + [nextv]
#                 else:
#                     queue.append((nextv, path + [nextv]))

    # def path_weight(self, path):
    #     # return [w for ]
    #     for v in path[:-1]:
    #         w = self.g[v]
