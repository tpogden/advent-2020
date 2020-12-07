
with open('data/05.txt') as f:
    arr = [l.strip() for l in f.readlines()]

def read_boarding_pass(bp):
    
    bp_row = bp[0:7]
    bp_col = bp[7:]

    bp_row = bp_row.replace('F', '0')
    bp_row = bp_row.replace('B', '1')
    bp_row = int(bp_row, 2)

    bp_col = bp_col.replace('L', '0')
    bp_col = bp_col.replace('R', '1')
    bp_col = int(bp_col, 2)

    return bp_row, bp_col

def get_seat_id(bp_row, bp_col):
    return bp_row*8 + bp_col

def read_boarding_passes(arr):

    seat_ids = [0]*len(arr)
    for i, bp in enumerate(arr):
        r, c = read_boarding_pass(bp)
        seat_ids[i] = get_seat_id(r, c)
    return max(seat_ids)

max_seat_id = read_boarding_passes(arr)

print('sol:', max_seat_id)
