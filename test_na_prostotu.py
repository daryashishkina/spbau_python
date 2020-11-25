def test(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

print('you can test 3 numbers:')
for d in range(3):
    x = int(input())
    print(test(x))

