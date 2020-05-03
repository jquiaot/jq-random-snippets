# fib.py - Fibonacci numbers exploration.
#

import sys

# Fibonacci calculator.
#
# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2)
#
def fib(n):
    if n >= 0:
        a = []
        if n >= 0:
            a.append(0)
        if n >= 1:
            a.append(1)
        for i in range(2, n+1):
            a.append(a[i-1]+a[i-2])
        return a[n]
    else:
        return 0


# Standard recursive version of Fibonacci. Will blow up your stack if called
# with sufficiently large n.
#
def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

# Memoized version of Fibonacci. Uses a dict to keep track of previously
# calculated values.
#
def fib_recur_memoized(n):
    d = {}
    d[0] = 0
    d[1] = 1
    return fib_recur_memoized_helper(n, d)

def fib_recur_memoized_helper(n, d):
    if n in d:
        return d[n]
    else:
        m = fib_recur_memoized_helper(n-1, d) + fib_recur_memoized_helper(n-2, d)
        d[n] = m
        return m

###
###

if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        for i in range(1, n+1):
            print('               fib({}) = {}'.format(i, fib(i)))
            print('         fib_recur({}) = {}'.format(i, fib_recur(i)))
            print('fib_recur_memoized({}) = {}'.format(i, fib_recur_memoized(i)))
    else:
        print('Usage: python fib.py n')
