#!/usr/bin/python3

def pascal(n):
	"""Returns a list of lists of integers representing the Pascal’s triangle of n"""
	pascal_triangle = [[1]]

	for i in range(n - 1):
		if len(pascal_triangle[-1]) > 1:
			last_item = pascal_triangle[-1]
			triangle = [1,]
			for index, j in enumerate(last_item):
				if index != (len(last_item) - 1):
					triangle.append(j + last_item[index + 1])
				else:
					break
				triangle.append(1)
				pascal_triangle.append(triangle)
		else:
			pascal_triangle.append([1,1])
	return pascal_triangle


for i in pascal(5):
	print(i)