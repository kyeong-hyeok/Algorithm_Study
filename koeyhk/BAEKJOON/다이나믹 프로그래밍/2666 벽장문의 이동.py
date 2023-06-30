import sys

input_data = sys.stdin.readline

N = int(input_data())
o1, o2 = map(int, input_data().split())
length = int(input_data())
order = []
for i in range(length):
    order.append(int(input_data()))
dp = [[] for i in range(21)]


def move(r, x, y, z):
    if order[x] <= y:
        dp[x].append((r + y - order[x], order[x], z))
    elif y < order[x] <= z:
        dp[x].append((r + z - order[x], y, order[x]))
        dp[x].append((r + order[x] - y, order[x], z))
    else:
        dp[x].append((r + order[x] - z, y, order[x]))
    return dp[x]


def use(x, a, b):
    if x == 0:
        return move(0, x, a, b)
    for o in dp[x-1]:
        r, f, s = o
        move(r, x, f, s)
    return dp[x]


for i in range(length):
    use(i, o1, o2)

dp[length-1].sort()
print(dp[length-1][0][0])