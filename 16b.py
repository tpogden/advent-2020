from collections import defaultdict

from operator import mul
from functools import reduce

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

def valid_ticket(ticket, rules):
    for i in ticket:
        if not val_valid_in_any_rule(val=i, rules=rules):
            return False
    return True

def valid_ticket_idxs(tickets, rules):
    return [i for i, t in enumerate(tickets) if valid_ticket(t, rules)]

def rule_valid_val_idxs_for_ticket(ticket, rule):
    return [i for i, val in enumerate(ticket) if 
        val_valid_in_rule(val=val, rule=rule)]

def rule_valid_val_idxs_for_tickets(tickets, rule):
    rule_idxs = []
    for t in tickets:
        rule_idxs.append(rule_valid_val_idxs_for_ticket(t, rule))
    return rule_idxs

def potential_idxs_for_rule(tickets, rule):
    pot_idxs = []
    rule_valid_idxs = rule_valid_val_idxs_for_tickets(tickets, rule)
    for i in range(len(tickets[0])):
        valid = all([i in t for t in rule_valid_idxs])
        if valid:
            pot_idxs.append(i)
    return set(pot_idxs)       

def find_idxs_for_rules(tickets, rules):

    def all_found(rule_pot_idxs):
        return all([len(v) == 0 for k, v in rule_pot_idxs.items()])

    rule_pot_idxs = dict()
    for k, v in rules.items():
        rule_pot_idxs[k] = potential_idxs_for_rule(tickets, rule=v)
    rule_valid_idxs = dict()
    while not all_found(rule_pot_idxs):
        for k, v in rule_pot_idxs.items():
            if len(v) == 1: # found a rule with only one potential idx left
                v2 = v.pop()
                break
        rule_valid_idxs[k] = v2
        for k2 in rule_pot_idxs:
            rule_pot_idxs[k2].discard(v2) # remove that idx from other rules
    return rule_valid_idxs

# rules, your_ticket, nearby_tickets = read_ticket(fpath='data/16-demo-b.txt')
rules, your_ticket, nearby_tickets = read_ticket(fpath='data/16.txt')

valid_ticket_idxs = valid_ticket_idxs(tickets=nearby_tickets, rules=rules)
valid_tickets = [t for i, t in enumerate(nearby_tickets) 
    if i in valid_ticket_idxs]
idxs = find_idxs_for_rules(tickets=valid_tickets, rules=rules)
your_ticket_vals = [your_ticket[v] for k,v in idxs.items() if 'departure' in k]
print('your_ticket_vals:', your_ticket_vals)
sol = reduce(mul, your_ticket_vals, 1)
print('sol:', sol)
