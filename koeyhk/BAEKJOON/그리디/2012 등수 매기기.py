import sys

N = int(input())
ranks = [int(sys.stdin.readline()) for i in range(N)]
ranks.sort()
result = 0
for i in range(N):
    result += abs(ranks[i] - (i+1))
print(result)
