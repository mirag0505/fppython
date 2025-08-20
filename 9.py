import functools

def odometer(oksana):
    speeds = oksana[0::2]
    times = oksana[1::2]
    deltas = [times[0]] + list(map(lambda x, y: x - y, times[1:], times[:-1]))
    distances = map(lambda s, d: s * d, speeds, deltas)
    return functools.reduce(lambda a, b: a + b, distances)

print(odometer([10,1,20,2]))