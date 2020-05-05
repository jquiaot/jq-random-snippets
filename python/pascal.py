# pascal.py - Pascal's triangle

# Given n >= 0, return Pascal's Triangle to the nth level, that is:
#
# n = 0:                    => []
# n = 1: 1
# n = 2: 1 1
# n = 3: 1 2 1
# n = 4: 1 3 3 1
# n = m: 1 (m-1)[0]+(m-1)[1] ... (m-1)[i-1]+(m-1)[i] 1
#
def pascals_triangle(n):
	p = []
	if n >= 1:
		p.append([1])
	for i in range(1, n):
		prev = p[-1]
		next = [1]
		for j in range(1, len(prev)):
			next.append(prev[j-1] + prev[j])
		next.append(1)
		p.append(next)
	return p

def pascals_triangle_generator(n):
	if n >= 1:
		yield [1]
	prev = [1]
	for i in range(1, n):
		next = [1]
		for j in range(1, len(prev)):
			next.append(prev[j-1] + prev[j])
		next.append(1)
		yield next
		prev = next

def test_pascals_triangle():
	for i in range(10):
		print("pascals_triangle(%s)           = %s" % (i, pascals_triangle(i)))

def test_pascals_triangle_generator():
	for i in range(10):
		print("pascals_triangle_generator(%s) = %s" % (i, list(pascals_triangle_generator(i))))

if __name__ == '__main__':
	test_pascals_triangle()
	test_pascals_triangle_generator()
