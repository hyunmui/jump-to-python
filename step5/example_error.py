# error.py

f = open('nofile', 'r')     # throw FileNotFoundError

a = 4 / 0       # throw ZeroDivisionError

x = [1, 2, 3]
x[4]            # throw IndexError


print('abcd')  # no execute after error
