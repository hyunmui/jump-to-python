# step 2-2. collection: list / tuple / dictionary /set

# unknown concept
# tuple: can't change item
# set: unordered, distincted


# minus index
a = [1, 2, 3, 4, 5]
print(a[-1], a[-2], a[-3])
print(a[0], a[1], a[2])

# slice
# 끝번호는 포함되지 않는다
print(a[0:2])
print(a[0:3])

# merge / concat
a = [1, 22, 333]
b = [7, 8]
print(a + b)

# repeat
print(a * 4)

# delete element
a = [1, 22, 333]
del a[1]
print(a)

# delete with slice
a = [1, 22, 333]
del a[1:]
print(a)

# function of list
# append, sort, reverse, index, insert, remove, pop, count, extend

# count
a = [1, 2, 3, 1]
print(a.count(1))

# extend
a = [1, 2, 3]
b = [1, 2, 4]
a.extend(b)
print(a)

print('=' * 50)
# end of list

# start set
s1 = set([1, 2, 3, 3])
print(s1)

s2 = set('Hello')
print(s2)


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('=' * 50)

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))

# 추가
s1.add(99)
s1.update([55, 66, 77])

print(s1)

# 제거
s1.remove(2)
print(s1)

print(type(s1))
