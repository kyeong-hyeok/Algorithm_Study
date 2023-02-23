import sys

N = int(input())
tips = [int(sys.stdin.readline()) for i in range(N)]
tips.sort(reverse=True)
result = 0
for i in range(N):
    money = tips[i]-i
    result += money if money > 0 else 0
print(result)