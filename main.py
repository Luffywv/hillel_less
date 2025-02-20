original_list = [1, 2, 3, 4, 5, 6]
if len(original_list) == 0:
    result = [[], []]
elif len(original_list) == 1:
    result = [original_list[:1], []]
else:
    middle = len(original_list) // 2
    result = [original_list[:middle], original_list[middle:]]

print(result)

# Если не парное число  элементов 

original_list = [1, 2, 3, 4, 5]
if len(original_list) == 0:
    result = [[], []]
elif len(original_list) == 1:
    result = [original_list[:1], []]
else:
    middle = len(original_list) // 2  # 5 // 2 = 2
    result = [original_list[:middle], original_list[middle:]]  # [:2] і [2:]

print(result)  # [[1, 2], [3, 4, 5]]

