# some tree traversal test code

# assume a binary tree is organized as an array:
#
#      0
#    1   2
#   3 4 5 6
# ...
#
# [0, 1, 2, 3, 4, 5, 6, ...]
#
# empty elements in the tree can be represented as None
#
# left_node(i) = 2 ** i + 1
# right_node(i) = 2 ** i + 2
#

# calculates the sum of the tree t rooted at index i
# this is the recursive version
#
def sum_tree(t, i):
  total = t[i]
  left_idx = 2 * i + 1
  right_idx = 2 * i + 2
  if left_idx < len(t):
    total += sum_tree(t, left_idx)
  if right_idx < len(t):
    total += sum_tree(t, right_idx)
  return total

def test_sum_tree(expected, tree):
  actual = sum_tree(tree, 0)
  print('test_sum_tree: tree={}, expected={}, actual={}'.format(tree, expected, actual))

if __name__ == '__main__':
  test_sum_tree(1, [1])
  test_sum_tree(3, [1,1,1])
  test_sum_tree(5, [1,1,1,1,1])


