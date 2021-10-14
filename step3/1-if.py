# if
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# 비교 연산자는 c 계열 언어와 같다

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# in 연산자
# in with array
print(1 in [1, 2, 3])       # expect True
print(1 not in [1, 2, 3])   # expect False
# in with string
print('j' not in 'python')  # expect True
# in with tuple
print('a' in ('a', 'b', 'c'))

print('-' * 20)
# If you have money in your pocket, take a taxi, if you don't, walk
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

print('-' * 20)
# pass
if 'money' not in pocket:
    pass
else:
    print('카드를 꺼내라')

print('-' * 20)
# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    if card:
        print('택시를 타고 가라')
    else:
        print('걸어가라')

# elif로 깔끔하게
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# 삼항연산자
score = 100
message = "success" if score >= 60 else "failure"
print('check: ' + message)
