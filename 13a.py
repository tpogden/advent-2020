def read_times(fpath='data/13-demo.txt'):
    with open(fpath) as f:
        now = int(f.readline().strip())
        buses = [int(i) for i in f.readline().strip().split(',') 
            if i is not 'x']
    return now, buses

# now, buses = read_times(fpath='data/13-demo.txt')
now, buses = read_times(fpath='data/13.txt')

print(now)
print(buses)

def next_time_bus(now, bus):
    prev = now//bus
    next = (prev + 1)*bus
    wait = next - now
    return wait, prev, next

nbt = next_time_bus(now, buses[0])

print(nbt)

def next_time_buses(now, buses):
    min_wait = 1000000
    min_next_bus = None
    for b in buses:
        wait, prev, next = next_time_bus(now, b)
        if wait < min_wait:
            min_wait = wait
            min_next_bus = b
    return min_wait, min_next_bus

min_wait, min_next_bus = next_time_buses(now, buses)

print(min_wait, min_next_bus)

print('sol:', min_wait*min_next_bus)
