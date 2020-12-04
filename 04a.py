
def read_passports(fpath='data/04-demo.txt'):
    with open(fpath) as f:
        all = f.read()
    arr = all.split('\n\n')
    ids = [a.replace('\n', ' ') for a in arr]
    kvs = [[kv.split(':') for kv in i.split(' ')] for i in ids]
    kvs[-1] = kvs[-1][:-1]
    return [dict(i) for i in kvs]

def validate_passport(p):
    REQ_KEYS_LIST = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    missing_keys = sum([bool(k not in p) for k in REQ_KEYS_LIST])
    if missing_keys != 0:
        return False
    return True

passports = read_passports('data/04.txt')
print('num passports:', len(passports))
print('sol:', sum([validate_passport(p) for p in passports]))
