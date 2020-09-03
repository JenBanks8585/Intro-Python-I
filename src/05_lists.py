# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# append at the end of the list

x.append(4)
print(x)


# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# add
x = x + y
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# pop index

x.pop(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
#insert at index, value 

x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE

print(len(x))

# Print all the values in x multiplied by 1000
# list comprehension

print ([i*1000 for i in x])