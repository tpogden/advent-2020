from collections import defaultdict

def read_ticket(fpath='data/16-demo.txt'):
    with open(fpath) as f:
        all = f.read()
        rules_str, your_ticket_str, nearby_str = all.split('\n\n')
    # Parse rules
    rules = rules_str.split('\n')
    rules = [r.split(': ') for r in rules]
    rules_dict = defaultdict(list)
    for r in rules:
        for i in r[1].split(' or '):
            lo, hi = i.split('-')
            rules_dict[r[0]].append(range(int(lo), int(hi)+1))
    print('rules_ticket:', rules_dict)
    # Parse your ticket
    your_ticket = your_ticket_str.lstrip('your ticket:\n').strip().split(',')
    your_ticket = [int(i) for i in your_ticket]
    print('your_ticket:', your_ticket)
    # Parse nearby
    nearby_tickets = nearby_str.lstrip('nearby tickets:\n').strip().split('\n')
    nearby_tickets = [s.split(',') for s in nearby_tickets]
    nearby_tickets = [[int(i) for i in t] for t in nearby_tickets]
    print('nearby_tickets:', nearby_tickets)
    return rules_dict, your_ticket, nearby_tickets

def val_valid_in_rule(val, rule):
    for r_range in rule:
        if val in r_range: # valid
            return True
    return False

def val_valid_in_any_rule(val, rules):
    for r in rules:
        if val_valid_in_rule(val, rules[r]):
            return True
    return False

def invalid_values(ticket, rules):
    invalid_vals = []
    for i in ticket:
        if not val_valid_in_any_rule(val=i, rules=rules):
            invalid_vals.append(i)
    return invalid_vals

def invalid_values_nearby(nearby_tickets, rules):
    invalid_vals = []
    for t in nearby_tickets:
        invalid_vals.extend(invalid_values(ticket=t, rules=rules))
    return invalid_vals

# rules, your_ticket, nearby_tickets = read_ticket(fpath='data/16-demo.txt')
rules, your_ticket, nearby_tickets = read_ticket(fpath='data/16.txt')

ivn = invalid_values_nearby(nearby_tickets=nearby_tickets, rules=rules)
print('sol:', sum(ivn))
