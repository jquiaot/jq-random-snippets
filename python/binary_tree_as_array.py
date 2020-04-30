# Python Binary Tree Summation
# ===

# Test code for summing up nodes in a binary tree. The binary tree is represented
# as an array of numbers.
#
#      0
#    1   2
#   3 4 5 6
#
# [0, 1, 2, 3, 4, 5, 6]
#
# empty elements in the tree can be represented as None, e.g.
#
#      0
#    1   2
#   3     6
#
# [0, 1, 2, 3, None, None, 6]
#
# The main thing to know is, given a node at index i, the left and right children
# can be found at:
#
# left_node(i) = 2 * i + 1
# right_node(i) = 2 * i + 2
#

# ===

# Calculates the sum of the tree t rooted at index i
# this is the recursive version
#
def sum_tree(t, i):
  total = 0
  if t[i]:
    total = t[i]
  left_idx = 2 * i + 1
  right_idx = 2 * i + 2
  if left_idx < len(t):
    total += sum_tree(t, left_idx)
  if right_idx < len(t):
    total += sum_tree(t, right_idx)
  return total

# Simple test function to exercise sum_tree() and compare it to some
# expected value.
#
def test_sum_tree(expected, tree):
  actual = sum_tree(tree, 0)
  print('test_sum_tree: tree={}, expected={}, actual={}'.format(tree, expected, actual))

# Run some tests.
#
if __name__ == '__main__':
  test_sum_tree(1, [1])
  test_sum_tree(3, [1,1,1])
  test_sum_tree(5, [1,1,1,1,1])
  test_sum_tree(15, [1, 2, 3, 4, None, None, 5])

