import sys
input = sys.stdin.readline

# 백 트래킹(DFS)
# Python3, pypy3 모두 통과
n = int(input())
nums = list(map(int, input().rstrip().split()))
op = list(map(int, input().rstrip().split())) # + - * / 의 개수

_max = -1e9
_min = 1e9

def dfs(depth, total, plus, minus, mul, div):
    global _max, _min

    if depth == n: # 리프 노드인 경우 = 모든 연산 종료
        _max = max(total, _max) #
        _min = min(total, _min)
        return # 재귀 종료

    # 주의) elif로 연결하면 안됨
    if plus:
        dfs(depth + 1, total + nums[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth + 1, total * nums[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, mul, div-1)

dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(_max)
print(_min)

# 순열
# Python3 시간초과, pypy3 통과
from itertools import permutations

n = int(input())
nums = list(map(int, input().rstrip().split()))
op_nums = list(map(int, input().rstrip().split())) # + - * / 의 개수
op_list = ['+', '-','*','/']
op = []

# 각 기호 개수만큼 op 리스트에 기호를 추가
for i in range(len(op_nums)):
    for j in range(op_nums[i]):
        op.append(op_list[i])

_max = -1e9
_min = 1e9

def solve():
    global _max, _min

    for case in permutations(op,n-1): # 주어진 기호 개수들로 만들 수 있는 모든 경우의 수

        # 각 기호 배치 순서에 맞춰 앞에서 부터 계산을 수행
        total = nums[0]

        for i in range(1, n):
            if case[i-1] == '+':
                total += nums[i]
            elif case[i-1] == '-':
                total -= nums[i]
            elif case[i-1] == '*':
                total *= nums[i]
            elif case[i-1] == '/':
                total = int(total / nums[i])

        # 계산 완료 후, 최대 최소 구하기
        _max = max(_max, total)
        _min = min(_min, total)

solve()
print(_max)
print(_min)


# 정리
# 음수를 양수로 나눌 때는, 음수를 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
print(-10//3) # -4 : 틀림
print(int(-10/3)) # 3 : 맞음
# int() 계산은 뒤에 소수점을 삭제함

