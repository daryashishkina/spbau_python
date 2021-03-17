import random
import time
import sys
import multiprocessing

n = 1000000
p = 27

def cats_cats(n):
    m = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            m += 1
    return m


def test_cats(pool):
    k = pool.map(cats_cats, [n] * p)
    return k


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    meow = 4*sum(test_cats(pool))/(n*p)
    print("number pi = ", meow)
    print("Time spent:", time.time() - t0)
else:
    print(__name__)
