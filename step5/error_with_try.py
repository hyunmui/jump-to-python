# error_with_try.py

try:
    f = open('nofile', 'r')     # throw FileNotFoundError
except:
    print('무언가 오류가 발생하였습니다')

try:
    a = 4 / 0       # throw ZeroDivisionError
except ZeroDivisionError:
    print('0으로 나눌수 없습니다')

try:
    x = [1, 2, 3]
    x[4]            # throw IndexError
except IndexError as e:
    print(e)

f = open('tmp/fileline.txt', 'r')
try:
    print('whatever run...')
except FileNotFoundError:
    print('No File')
finally:
    f.close()

# multiple errors
try:
    x = [1, 2, 3]
    x[4]            # throw IndexError
    a = 4 / 0       # throw ZeroDivisionError
except (IndexError, ZeroDivisionError) as e:
    print(e)


class Bird:
    def fly(self):
        # raise NotImplementedError
        print('very fast')


class Eagle(Bird):
    pass


b = Eagle()
b.fly()


# custom exception
class MyError(Exception):
    def __str__(self) -> str:
        return 'Not allowed Nickname'


def say_nick(nick):
    if nick == 'foo':
        raise MyError()
    print(nick)


try:
    say_nick('Martin')
    say_nick('foo')
except MyError as e:
    print(e)
