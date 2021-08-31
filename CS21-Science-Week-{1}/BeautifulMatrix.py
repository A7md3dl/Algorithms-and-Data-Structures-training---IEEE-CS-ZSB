matrix = []
for i in range(5):
	matrix.append([int(i) for i in input().split(' ')])
x, y = (0, 0)
for i in range(5):
	if matrix[i].count(1) > 0:
		y, x = (i, matrix[i].index(1))
print(abs(2-y)+abs(2-x))
