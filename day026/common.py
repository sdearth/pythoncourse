with open("file1.txt") as file1:
    list_1 = file1.readlines()

with open("file2.txt") as file2:
    list_2 = file2.readlines()

result = [int(num) for num in list_1 if num in list_2]
print(result)