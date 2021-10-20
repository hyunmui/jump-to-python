# args.py

import sys

# catch args for batch / shell script
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
