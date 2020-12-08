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

def create_bags_edgelist_weighted(rules_dict):
    edgelist = []
    for k, v in rules_dict.items():
        for i in v:
            if i[0] == 'no':
                weight = 0
            else:
                weight = int(i[0])
            edgelist.append((k, i[1], weight))
    return edgelist

# rules_dict = read_rules(fpath='data/07-demo.txt')
# rules_dict = read_rules(fpath='data/07-demo-b.txt')
rules_dict = read_rules(fpath='data/07.txt')

edgelist = create_bags_edgelist_weighted(rules_dict)

g = Graph(directed=True, edgelist=edgelist)

print(g)

def num_contains(g, bag):
    total_bags = 0
    for i in g.g[bag]:
        num_bags_dir_inside = g.weights[bag, i]
        # print('bag:', bag, '; i:', i, 
        #     '; num_bags_dir_inside: ', num_bags_dir_inside)
        if num_bags_dir_inside != 0:
            total_bags +=  (num_bags_dir_inside + 
                num_bags_dir_inside*num_contains(g, i))
    return total_bags 

sol = num_contains(g=g, bag='shiny gold')
print('sol:', sol)

# dotrepr = g.dot_repr()

# with open('dotrepr.txt', 'w') as f:
#     f.write(dotrepr)
