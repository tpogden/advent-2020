CHARS = 'abcdefghijklmnopqrstuvwxyz'

def read_decl_forms(fpath='data/06.txt'):
    with open(fpath) as f:
        all = f.read()
    arr = all.split('\n\n')
    group_dfs = [a.split('\n') for a in arr]
    group_dfs[-1] = group_dfs[-1][:-1]
    return group_dfs

def count_group_char(c, group_df):
    return sum([c in df for df in group_df])

def count_group_chars(group_df):
    dict_count = dict()
    for c in CHARS:
        dict_count[c] = count_group_char(c, group_df)
    return dict_count

def all_ans_count(group_df):
    print(group_df)
    n = len(group_df)
    print(n)
    dict_count = count_group_chars(group_df)
    return list(dict_count.values()).count(n)

group_dfs = read_decl_forms()

sol = sum([all_ans_count(gdf) for gdf in group_dfs])
print('sol:', sol)
