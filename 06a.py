
def read_decl_forms(fpath='data/06.txt'):
    with open(fpath) as f:
        all = f.read()
    arr = all.split('\n\n')
    group_dfs = [a.replace('\n', '') for a in arr]
    return group_dfs
    # print(group_dfs)
    # dfa = [set(i) for i in group_dfs]

def unique_answers(group_dfs):
    dfa = [set(i) for i in group_dfs]
    print(dfa)    
    return sum([len(j) for j in dfa])

group_dfs = read_decl_forms()

print(group_dfs)

sol = unique_answers(group_dfs)

print(sol)
