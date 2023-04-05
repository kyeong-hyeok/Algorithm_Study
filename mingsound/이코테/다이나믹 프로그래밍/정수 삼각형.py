# 4:11 - 4:17

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def solution():
    for i in range(n-2, -1, -1): # 맨 아래에서 2번째부터
        for j in range(i+1): # 각 열마다
            arr[i][j] = arr[i][j] + max(arr[i+1][j], arr[i+1][j+1]) # 점화식 : 왼쪽 오른쪽 중에서 큰 것을 더한다.

    return arr[0][0] # 최댓값은 맨 꼭대기 값

print(solution())

