import math
import random
import sys

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

###############################################################################

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

###############################################################################

# Performs quicksort on the specified list of integers. Tries to follow the
# algorithm specified in CLR (1st ed.), p. 154.
#
# Time complexity: Θ(n lg n) average case
# Space complexity: O(1) - sorts in place
#
def quicksort(a):
	if a:
		quicksort_helper(a, 0, len(a) - 1)
	return a

def quicksort_helper(a, p, r):
	if p < r:
		# partition a around some pivot
		q = qs_partition(a, p, r)
		# then recursively invoke quicksort on subarrays to left of and right
		# of pivot
		quicksort_helper(a, p, q)
		quicksort_helper(a, q+1, r)

# Partitions the subarray a[p..r].
#
def qs_partition(a, p, r):
	# pick the pivot
	x = a[p]
	# position pointers i and j just outside our range p..r
	i = p - 1
	j = r + 1
	while True:
		j -= 1
		while a[j] > x:
			# work from j downwards, looking for a value <= our pivot
			j -= 1
		i += 1
		while a[i] < x:
			# work from i upwards, looking for a value >= our pivot
			i += 1
		if i < j:
			# swap i and j
			tmp = a[i]
			a[i] = a[j]
			a[j] = tmp
		else:
			# we've found our partition point
			return j

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

# Asserts the specified list is sorted in ascending order (a[i-1] <= a[i] for i in range(1, len(a)))
#
def assert_is_sorted(l):
	print(l)
	for i in range(1, len(l)):
		assert l[i-1] <= l[i]

# Executes the sort methods
#
def run_sorts(n):
	a = make_random_array(n)

	b = insertion_sort(a.copy())
	assert_is_sorted(b)

	c = merge_sort(a.copy())
	assert_is_sorted(c)

	d = quicksort(a.copy())
	assert_is_sorted(d)

###
###

if __name__ == '__main__':
	n = 100
	if len(sys.argv) == 2:
		n = int(sys.argv[1])
	run_sorts(n)

# END
