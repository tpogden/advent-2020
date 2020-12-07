from utils import GraphWeighted 

def read_rules(fpath='data/07-demo.txt'):
    with open(fpath) as f:
        rules_str = [l.strip() for l in f.readlines()]
    rules_dict = dict()
    for rs in rules_str:
        bag_str, contents_str = rs.split(' bags contain ')
        contents_str = contents_str.strip('.')
        contents_list = contents_str.split(', ')
        contents_list = [c.replace(' bags', '') for c in contents_list]
        contents_list = [c.replace(' bag', '') for c in contents_list]
        contents_list = [c.split(' ', 1) for c in contents_list]
        rules_dict[bag_str] = contents_list
    return rules_dict

def create_bags_edgelist_weighted(rules_dict):
    edgelist = []
    for k, v in rules_dict.items():
        for i in v:
            edgelist.append((k, i[1], i[0]))
    return edgelist

rules_dict = read_rules(fpath='data/07-demo-b.txt')
print(rules_dict)

edgelist = create_bags_edgelist_weighted(rules_dict)
print('EDGELIST')
print(edgelist)

g = GraphWeighted(directed=True, edgelist=edgelist)

# g.insert_edge(x='a', y='b', weight=2)

# print(g.edgelist())

# print(g.g)

print(g)

path = ['shiny gold', 'dark red']

pw = g.path_weight(path)

print(pw)

# v = g.bfs(start='shiny gold')
# print(v)
