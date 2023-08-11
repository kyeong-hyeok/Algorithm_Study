import sys

input_data = sys.stdin.readline

N = int(input_data())
black = [[0] * 100 for _ in range(100)]
result = 0
for _ in range(N):
    a, b = map(int, input_data().split())
    for i in range(b, b + 10):
        for j in range(a, a + 10):
            if black[i][j] == 0:
                black[i][j] = 1
                result += 1

print(result)