# min_steps_to_one.py
#
# Given a number n, 1 <= n <= 1000000, what are the minimum number of steps
# needed to get to 1, using the following operations:
#
# 1. Divide by 3, iff n is divisible by 3 (i.e., n % 3 == 0)
# 2. Divide by 2, iff n is divisible by 2 (i.e., n % 2 == 0)
# 3. Subtract 1
#
# Examples:
#
# 5 ->[-1]-> 4 ->[/2]-> 2 ->[-1]-> 1 == 3 steps
# 10 ->[-1]-> 9 ->[/3]-> 3 ->[/3]-> 1 == 3 steps
#

# Recursive version with memoization.
#
# Time complexity: O(k^n)
# Space complexity: O(n)
#
def min_steps_to_one_recur(n):
    cache = {}
    return min_steps_to_one_recur_helper(n, cache)

def min_steps_to_one_recur_helper(n, cache):
    if n == 1:
        return 0
    if n in cache:
        return cache[n]
    steps = min_steps_to_one_recur_helper(n - 1, cache)
    if n % 2 == 0:
        steps_by_two = min_steps_to_one_recur_helper(n / 2, cache)
        steps = steps if steps < steps_by_two else steps_by_two
    if n % 3 == 0:
        steps_by_three = min_steps_to_one_recur_helper(n / 3, cache)
        steps = steps if steps < steps_by_three else steps_by_three
    cache[n] = steps + 1
    return steps + 1

# Tabulation version (dynamic programming).
#
# Time complexity: O(n)
# Space complexity: O(n)
#
def min_steps_to_one_dynamic(n):
    s = [None] * (n + 1)
    s[0] = None
    s[1] = 0 # base case
    for i in range(2, n + 1):
        s0 = s[i - 1]
        s1 = s[int(i / 3)] if i % 3 == 0 else None
        s2 = s[int(i / 2)] if i % 2 == 0 else None
        min = s0
        if s1 is not None and s1 < min:
            min = s1
        if s2 is not None and s2 < min:
            min = s2
        s[i] = min + 1
    return s[n]

# Paths (also dynamic programming).
#
# Time complexity:
# Space complexity:

def min_steps_to_one_paths(n):
    if n == 1:
        return 0
    # map of optimal paths from some key n, used for pruning the path space
    optimal_paths = {}
    # current set of paths we're exploring
    paths = [[n, 0]]
    while True:
        # for each iteration, figure out the viable paths by
        # extending all current paths and comparing with collected
        # optimal paths
        candidate_paths = []
        for path in paths:
            new_paths = expand_paths(path)
            if new_paths:
                for new_path in new_paths:
                    if new_path[0] in optimal_paths:
                        if new_path[1] < optimal_paths[new_path[0]]:
                            optimal_paths[new_path[0]] = new_path[1]
                            candidate_paths.append(new_path)
                    else:
                        optimal_paths[new_path[0]] = new_path[1]
                        candidate_paths.append(new_path)
        # check and see if we've made it to the end
        optimal_length = None
        for path in candidate_paths:
            if path[0] == 1:
                if optimal_length is None or path[1] < optimal_length:
                    optimal_length = path[1]
        if optimal_length is not None:
            return optimal_length
        else:
            paths = candidate_paths

# Given a path p = [m, s] where m is the current value and s is the number
# of steps taken so far to reach that value, return the list of possible
# paths given the operations.
#
def expand_paths(p):
    paths = []
    if p[0] % 3 == 0:
        paths.append([int(p[0] / 3), p[1] + 1])
    if p[0] % 2 == 0:
        paths.append([int(p[0] / 2), p[1] + 1])
    paths.append([p[0] - 1, p[1] + 1])
    return paths

def test_min_steps_to_one(n):
    print('min_steps_to_one_dynamic({}) = {}'.format(n, min_steps_to_one_dynamic(n)))
    print('min_steps_to_one_recur({}) = {}'.format(n, min_steps_to_one_recur(n)))
    print('min_steps_to_one_paths({}) = {}'.format(n, min_steps_to_one_paths(n)))

if __name__ == '__main__':
    test_min_steps_to_one(500)
