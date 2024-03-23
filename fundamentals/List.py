numbers = [13, 2, 33, 14, 65, 26, 47, 98, 19]
numbers.sort(reverse=False)  # [2, 13, 14, 19, 26, 33, 47, 65, 98]
print(numbers)

numbers.sort(reverse=True)  # [98, 65, 47, 33, 26, 19, 14, 13, 2]
print(numbers)

print(numbers[2:5])  # [47, 33, 26]
print(numbers[3:6])  # [33, 26, 19]
print(numbers[5:])  # [19, 14, 13, 2]
print(numbers[-2:])  # [13, 2]
print(numbers[:-2])  # [98, 65, 47, 33, 26, 19, 14]

mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(len(mylist))
print(mylist[len(mylist) - 1])

mylist.remove("apple")
print(mylist)
