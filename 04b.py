
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

    # byr
    valid_byr = ((len(p['byr']) == 4) and (p['byr'] >= '1920') and 
        (p['byr'] <= '2002'))
    if not valid_byr:
        print('invalid byr:', p['byr'])
        return False

    # iyr
    valid_iyr = ((len(p['iyr']) == 4) and (p['iyr'] >= '2010') and 
        (p['iyr'] <= '2020'))
    if not valid_iyr:
        print('invalid iyr:', p['iyr'])
        return False

    # eyr
    valid_eyr = ((len(p['eyr']) == 4) and (p['eyr'] >= '2020') and 
        (p['eyr'] <= '2030'))
    if not valid_eyr:
        print('invalid eyr:', p['eyr'])
        return False

    # hgt
    hgt_val = p['hgt'][:-2]
    hgt_met = p['hgt'][-2:]
    valid_hgt = False
    if hgt_met == 'cm' and hgt_val >= '150' and hgt_val <= '193':
        valid_hgt = True
    if hgt_met == 'in' and hgt_val >= '59' and hgt_val <= '76':
        valid_hgt = True
    if not valid_hgt:
        print('invalid hgt:', p['hgt'])
        return False    

    # hcl
    hexdigits = '0123456789abcdef'
    valid_hcl = (p['hcl'][0] == '#' and 
        all([c in hexdigits for c in ['ecl'][1:]]))
    if not valid_hcl:
        print('invalid hcl:', p['hcl'])
        return False

    # ecl
    valid_ecl = p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not valid_ecl:
        print('invalid ecl:', p['ecl'])
        return False

    # pid
    valid_pid = ((len(p['pid']) == 9) and p['pid'].isdigit())
    if not valid_pid:
        print('invalid pid:', p['pid'])
        return False

    return True

passports = read_passports(fpath='data/04.txt')
print('num passports:', len(passports))
print('sol:', sum([validate_passport(p) for p in passports]))
