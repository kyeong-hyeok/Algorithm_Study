N = list(map(int, input()))
L = len(N) // 2
result = 0
for i in range(L):
    result += N[i]
    result -= N[L+i]
if result == 0:
    print("LUCKY")
else:
    print("READY")

