from utils import Graph 

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

def get_bags_keys(rules_dict):
    return list(rules_dict.keys())

def create_bags_edgelist(rules_dict):

    edgelist = []
    for k, v in rules_dict.items():
        for i in v:
            edgelist.append((k, i[1]))
    return edgelist

def create_bags_graph(edgelist):
    g = Graph(directed=True, edgelist=edgelist)
    return g

# rules_dict = read_rules()
# rules_dict = read_rules(fpath='data/07-test.txt')
rules_dict = read_rules(fpath='data/07.txt')

print(rules_dict)

edgelist = create_bags_edgelist(rules_dict)

g = create_bags_graph(edgelist)
print('\ng0:\n', g.dot_repr(), '\n')

bags_keys = get_bags_keys(rules_dict)

GOAL = 'shiny gold'

num_bag_colors = 0
for k in bags_keys:
    paths = list(g.bfs_paths(start=k, goal=GOAL))
    # print(paths)
    if len(paths) > 0:
        num_bag_colors += 1
print('num_bag_colors:', num_bag_colors)
