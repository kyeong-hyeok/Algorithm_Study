import sys

input_data = sys.stdin.readline

N = int(input_data())
sang = list(map(int, input_data().split()))
d = {}
for s in sang:
    d[s] = 1
M = int(input_data())
check = list(map(int, input_data().split()))
for c in check:
    print('1' if c in d else '0', end=' ')
