import sys

input_data = sys.stdin.readline


def factorial(a):
    if a < 2:
        return 1
    else:
        return a * factorial(a-1)


T = int(input_data())
for i in range(T):
    N, M = map(int, input_data().split())
    result = int(factorial(M) / ((factorial(M - N)) * factorial(N)))
    print(result)