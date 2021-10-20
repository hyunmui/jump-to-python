# 1-def.py

def say():
    print('Hi')


say()


def add(a, b):
    return a+b


result = add(3, 5)

print(result)


def add_many(*args):
    # variable parameters
    result = 0
    for i in args:
        result = result + i
    return result


print(add_many(3, 6, 9))
print(add_many(1, 2, 3, 4, 5))


def print_kwargs(**kwargs):
    # keyword parameters
    print(kwargs)


print_kwargs(a=1, b="hello")


def add_and_mul(a, b):
    return a+b, a*b     # (a+b, a*b) --> tuple


result = add_and_mul(3, 4)
print(result)

add_result, mul_result = add_and_mul(5, 7)
print(add_result, mul_result)


def say_myself(name, old, man=True):
    print('My name is %s' % name)
    print('I am %d years old' % old)
    if man:
        print("I'am a man")
    else:
        print("I'am woman")


say_myself('선현민', 35)
say_myself('아이유', 29, False)
say_myself('선은진', man=False, old=37)


# lambda
add = lambda a,b : a+b

print(add(3,4))