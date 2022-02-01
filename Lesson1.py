def path_length(point_1, point_2):
	#	 подстановка значений в формулу
	result = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
	# результат – 3.605551275463989
	return result

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

points = {1: (0, 2), 2: (2, 5), 3: (5, 2), 4: (6, 6), 5: (8, 3)}

point_range = [
	[0, path_length(points[1], points[2]), path_length(points[1], points[3]), path_length(points[1], points[4]), path_length(points[1], points[5])],
	[path_length(points[2], points[1]), 0, path_length(points[2], points[3]), path_length(points[2], points[4]), path_length(points[2], points[5])],
	[path_length(points[3], points[1]), path_length(points[3], points[2]), 0, path_length(points[3], points[4]), path_length(points[3], points[5])],
	[path_length(points[4], points[1]), path_length(points[4], points[2]), path_length(points[4], points[3]), 0, path_length(points[4], points[5])],
	[path_length(points[5], points[1]), path_length(points[5], points[2]), path_length(points[5], points[3]), path_length(points[5], points[4]), 0]
]


counter = 0
path = []
min_path = []
point_distance = []
min_path_distance = 10000
min_counter = 0


for i1 in range(1):
	for i2 in range(5):
		for i3 in range(5):
			for i4 in range(5):
				for i5 in range(5):
					if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i3 != i4) and (i3 != i5) and (i4 != i5) :
						path.append([i1 + 1, i2 + 1, i3 + 1, i4 + 1, i5 + 1, i1 + 1])
						if (point_range[i1][i2] + point_range[i2][i3] + point_range[i3][i4] + point_range[i4][i5] + point_range[i5][i1]) < min_path_distance :
								min_path_distance = point_range[i1][i2] + point_range[i2][i3] + point_range[i3][i4] + point_range[i4][i5]  + point_range[i5][i1]
								min_counter = counter
								min_path = path[min_counter]
								intermediate_distance = 0
								point_distance.clear()
								intermediate_distance += point_range[i1][i2]
								point_distance.append(intermediate_distance)
								intermediate_distance += point_range[i2][i3]
								point_distance.append(intermediate_distance)
								intermediate_distance += point_range[i3][i4]
								point_distance.append(intermediate_distance)
								intermediate_distance += point_range[i4][i5]
								point_distance.append(intermediate_distance)
								intermediate_distance += point_range[i5][i1]
								point_distance.append(intermediate_distance)
						counter +=1

print(min_path[0], ' -> ', min_path[1], '[', point_distance[0], ']', ' -> ', min_path[2], '[', point_distance[1], ']', ' -> ', min_path[3], '[', point_distance[2], ']', ' -> ', min_path[4], '[', point_distance[3], ']', ' -> ', min_path[5], '[' , min_path_distance, ']')