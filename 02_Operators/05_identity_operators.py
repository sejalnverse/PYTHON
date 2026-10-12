# 1. is operator
a = [1, 2, 3]
b = a

print(a is b)

# 2. is not operator
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)

# 3. Compare two separate lists
a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)

# 4. Check the same object
x = [5, 10]
y = x

print(x is y)
print(x == y)

# 5. Check different objects
x = [1, 2, 3]
y = [4, 5, 6]

print(x is y)
print(x is not y)