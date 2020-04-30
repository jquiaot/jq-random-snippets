# rectangle_finder.py - given a 2d array (array of arrays) of ints of 1's and 0's, find the rectangles
# consisting of 0's
#
def solve():
  image1 = [
    [0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
  ]

  image2 = [
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  ]
  rects = find_rectangles(image1)
  print(rects)

  rects = find_rectangles(image2)
  print(rects)

# Given an array of arrays of ints representing a 2D image consisting of 1's and 0's, where 0's
# are arranged in distinct rectangles, find and return all such rectangles.
#
def find_rectangles(img):
  rects = []
  for y in range(len(img)):
    for x in range(len(img[y])):
      if img[y][x] == 0 and not is_overlap(rects, x, y):
        # print("Found 0 at ({},{})".format(x, y))
        rects.append(find_rectangle(img, x, y))
  return rects

# Returns True if the coordinates (x, y) overlap with any rectangles in rects.
#
def is_overlap(rects, x, y):
  for rect in rects:
    if rect[0] <= x and rect[2] >= x and rect[1] <= y and rect[3] >= y:
      return True
  return False

# Given a 2D image array and the upper left coordinates of a "zero" rectangle, find the lower 
# right coordinates and return a 4-element integer array representing [x0, y0, x1, y1].
#
# (x0, y0) = upper-left
# (x1, y1) = lower_right
#
def find_rectangle(img, x0, y0):
  x1 = -1
  y1 = -1
  for x_tmp in range(x0, len(img[y0]), 1):
    # print("Checking {},{}={}".format(y0, x_tmp, img[y0][x_tmp]))
    if img[y0][x_tmp] == 1:
      x1 = x_tmp - 1
      break
  if x1 == -1:
    x1 = len(img[y0]) - 1
  for y_tmp in range(y0, len(img), 1):
    # print("Checking {},{}={}".format(y_tmp, x0, img[y_tmp][x0]))
    if img[y_tmp][x0] == 1:
      y1 = y_tmp - 1
      break
  if y1 == -1:
    y1 = len(img)
  return [x0, y0, x1, y1]

if __name__ == '__main__':
  solve()

