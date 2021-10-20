# FourCal.py

class FourCal:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    # def setdata(self, first, last):
    #     self.first = first
    #     self.last = last

    def add(self):
        return self.first + self.last

    def sub(self):
        return self.first - self.last

    def mul(self):
        return self.first * self.last

    def div(self):
        return self.first / self.last

    def test(str):
        print('this is test strings : %s' % str)


a = FourCal(5, 2)

print(type(a))

# a.setdata(5, 2)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())


# run like static method
FourCal.test('haha hoho')

# run method with instance and Class Method Definition
print(FourCal.add(a))


# inheritance

class MoreFourCal(FourCal):
    VERSION = "1.0.0"
    # append method

    def pow(self):
        return self.first ** self.last

    # method override
    def div(self):
        return super().div() if self.last != 0 else 0


b = MoreFourCal(2, 10)

print(b.div())
print(b.pow())

c = MoreFourCal(2, 0)
c2 = MoreFourCal(12, 2)

print(c.div())
print(c2.div())
print(MoreFourCal.VERSION)
MoreFourCal.VERSION = "2.0.1"   # not safe
print(c2.VERSION)
