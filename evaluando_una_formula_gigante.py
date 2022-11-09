

if __name__ == '__main__':
    x, y, z = [float(x) for x in input().split()]
    p1 = (2 * x + y) / z
    p2 = (y**3 - z)
    p1 = p1 * p2
    p3 = x + 2 * y + 3 * z
    p4 = z - 2 * y - 3 * x
    p3 = p3 / p4
    r = p1 / (p3 + x * x + z * z)
    print(r)
