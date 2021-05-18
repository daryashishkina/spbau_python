import math
def test_w(n):
    if (math.factorial(n-1)+1) % n!=0:
        return False
    else:
        return True

print('you can test 3 numbers')
for i in range(3):
    x = int(input())
    print(test_w(x))