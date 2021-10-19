# 1-2.vartest.py

a = 1


def vartest(a):
    # call by value
    a = a+1


vartest(a)
print(a)


def vartest_global(a):
    global a
    a = a+1
