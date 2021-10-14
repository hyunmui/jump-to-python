# 3-for.py

# iterate list
from common import print_line


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print_line()

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

print_line()

# 합격 / 불합격 여부 출력(60점 이상)
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('%d: 합격' % number)
    else:
        print('%d: 불합격' % number)

print_line()

# my style
number = 0
for mark in marks:
    number = number + 1
    message = '합격' if mark >= 60 else '불합격'
    print(f"{number}: {message}")

# continue 문 지원

print_line()

# range
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print('-' * 10)

print_line()

# list 내포 사용
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

result2 = [num * 3 for num in a]
print(result2)
# only even number
result3 = [num * 3 for num in a if num % 2 == 0]
print(result3)

# 구구단 결과 담기
result4 = [x*y for x in range(2, 10)
           for y in range(1, 10)]
print(result4)

# 구구단 자체 담기
result5 = [(x, y, x*y)for x in range(2, 10)
           for y in range(1, 10)]
print(result5)

for row in result5:
    print(f"{row[0]} x {row[1]} = {row[2]}")
