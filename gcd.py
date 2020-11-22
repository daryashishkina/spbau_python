def gcd(a, b):
    if a == 0 or b == 0: 
         return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)

print('examples: ')
h = gcd(68, 352)
print('gcd(68, 352) = ', h)

k = gcd(76, 38)
print('gcd(76, 38) = ', k)

s = gcd(105, 168)
print('gcd(105, 168) = ', s)
