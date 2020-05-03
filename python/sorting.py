import math
import random

# sorting.py - Various sorting algorithms, for practice.
#

# These sorting algorithms take a list of integers, and sort the list, in 
# ascending order.

###############################################################################

# Performs insertion sort on the specified list of integers.
#
# Time complexity:  O(n^2)
# Space complexity: O(1) - we don't use any extra space to sort
#
def insertion_sort(a):
	for j in range(1, len(a)):
		val = a[j]
		i = j - 1
		while i >= 0 and a[i] > val:
			a[i+1] = a[i]
			i -= 1
		a[i+1] = val
	return a

# Performs merge sort on the specified list of integers.
#
# Time complexity:  O(n log(n))
# Space complexity: O(n) - we're creating extra storage in each merge 
#                   operation that is proportional to n
#
def merge_sort(a):
	if len(a) <= 1:
		# base case - a is 0 or 1 elements, nothing to merge, just return it
		return a
	else:
		# else a has more than 1 element, so need to:
		# 1. find the approximate midpoint
		# 2. split a into two pars at the midpoint
		# 3. recursively call merge_sort on the two parts
		# 4. merge the two parts back
		q = int(math.floor(len(a) / 2))
		left = merge_sort(a[:q])
		right = merge_sort(a[q:])
		return merge(left, right)

# Return the merger of the two lists, elements in ascending order.
#
def merge(l, r):
	merged = []
	lidx = 0
	ridx = 0
	while lidx < len(l) and ridx < len(r):
		if l[lidx] <= r[ridx]:
			merged.append(l[lidx])
			lidx += 1
		else:
			merged.append(r[ridx])
			ridx += 1
	# we've exhausted one or more of the lists, so just merge the rest
	if lidx < len(l):
		merged.extend(l[lidx:])
	if ridx < len(r):
		merged.extend(r[ridx:])
	return merged

###
###

# test code

# Generates a random array of n elements, using the value space from 0 - n^2
#
def make_random_array(n):
	a = []
	for i in range(n):
		a.append(int(random.random() * n * n))
	return a

def assert_is_sorted(l):
	for i in range(1, len(l)):
		assert l[i-1] <= l[i]

# Executes the sort methods
#
def run_sorts():
	a = make_random_array(1000)
	print(a)

	b = merge_sort(a.copy())
	print(b)
	assert_is_sorted(b)

	c = insertion_sort(a.copy())
	print(c)
	assert_is_sorted(c)

###
###

if __name__ == '__main__':
	run_sorts()

# END
