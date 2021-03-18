# list comprehension takes forms:
#   new_list = [new_item for item in list]
#   new_list = [new_item for item in list for test]

nums = [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
sq = [num**2 for num in nums]
print(sq)

even = [num for num in nums if num % 2 == 0]
print(even)