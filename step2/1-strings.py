# step 2-1. strings

# string multiline
multiline = '''
Life is too short
You need python
\test
\\test
"test"
'test'
'''

print(multiline)

# string multiply
print('=' * 40)
print(multiline * 2)
print('=' * 40)

# string length
loremLength = len('Lorem, ipsum dolor sit amet consectetur adipisicing elit. Laboriosam praesentium quam libero odio, cum provident dolor necessitatibus soluta repellat, placeat architecto dignissimos in ex. Vel maxime inventore porro. Minus, placeat.')


print(f"lorem len: {loremLength}")      # formatting #1 - upper 3.6
print('lorem len: %d' % loremLength)    # formatting #2
print('pi value: %s' % 3.1412)          # formatting #2-1
print('lorem len: {len}'.format(len=loremLength))   # formatting #3

# arrange strings - left
print('{0:<10}'.format('hi'))
# arrange strings - right
print('{0:>10}'.format('hi'))
# arrange strings - center
print('{0:^10}'.format('hi'))

# arrange string and fill - left
print(f'{"hi":=<10}')
# arrange string and fill - right
print(f'{"hi":@>10}')
# arrange string and fill - center
print(f'{"hi":!^10}')


# find index
a = 'Python is the best choice'
print(a.find('be'))
print(a.find('nodata'))
print(a.index('be'))
# print(a.index('nodata'))  # raise error


# trim
a = '  hi  '
print(a.lstrip())   # trim left
print(a.rstrip())   # trim right
print(a.strip())    # trim both

# split sentences
a = "Life is too short"
print(a.split())
b = "a/b/c/d"
print(b.split('/'))
