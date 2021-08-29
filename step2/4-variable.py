# variable

# memory address check
from copy import copy
a = [1, 2, 3]
print(id(a))

# copy value vs reference
b = a
print(a is b)   # true
print(id(a), id(b))  # equal memory address

c = [1, 2, 3]
print(a == c, a is c)

# deep copy
b = a[:]
b[1] = 4
print(a, b)

x = copy(a)
x[2] = 99
print(a, x)


# multiple declare
a, b = ('python', 'life')
(a, b) = 'python', 'life'
print(a, b)

[i, j, k] = x   # [1,2,99]
print(i, j, k)

a = b = 'python'
print(a, b)

# swap
a = 3
b = 5
a, b = b, a
print(a, b)
