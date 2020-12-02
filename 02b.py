with open('data/02.txt') as f:
    arr = [l.strip().split() for l in f.readlines()]

valid = 0
for p in arr:
    pc1, pc2 = p[0].split('-')
    pc1, pc2 = int(pc1), int(pc2)
    c = p[1][:-1]
    pw = p[2]
    # print(pc1, pc2)
    if bool(pw[pc1-1] == c) != bool(pw[pc2-1] == c): # xor
        valid += 1
        print('valid:', p)

print('sol:', valid)

