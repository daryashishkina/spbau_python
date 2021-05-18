def egcd(a,b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = egcd(b, a % b)
        return d, y , x - y * (a // b)

print('examples:')
h = egcd(68, 352)
print('gcd(68, 352) = ', h)

k = egcd(76, 38)
print('gcd(76, 38) = ', k)

s = egcd(105, 168)
print('gcd(105, 168) = ', s)