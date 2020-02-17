# Gladys Morales
# February 11th, 2020
#This program writes a loop that prints each number and its square on a new line.

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in nums:
    print(i)

squared = []

for i in nums:
    sqr = i * i
    squared.append(sqr)
    print("The square of {} is {}".format(i, sqr))