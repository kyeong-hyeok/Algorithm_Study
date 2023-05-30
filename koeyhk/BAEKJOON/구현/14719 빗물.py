import sys

input_data = sys.stdin.readline

H, W = map(int, input_data().split())
block = list(map(int, input_data().split()))

result = 0
for i in range(1, W-1):
    left = max(block[:i])
    right = max(block[i+1:])
    min_block = min(left, right)
    if block[i] < min_block:
        result += min_block - block[i]

print(result)