with open('data/02.txt') as f:
    arr = [l.strip().split() for l in f.readlines()]

valid = 0
for p in arr:
    pcmin, pcmax = p[0].split('-')
    c = p[1][:-1]
    pw = p[2]
    cnt = pw.count(c)
    if cnt >= int(pcmin) and cnt <= int(pcmax):
        valid += 1
        print('valid:', p)

print('sol:', valid)
