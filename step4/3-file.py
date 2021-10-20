# 3-file.py

from os import read

f = open('tmp/newfile.txt', 'w')
f.close()

path = 'tmp/flieline.txt'

f = open(path, 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close()

# readline with while
f = open(path, 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()

# readlines
f = open(path, 'r')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()

# read
f = open(path, 'r')
data = f.read()
print(data)
f.close()

# append
f = open(path, 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()
