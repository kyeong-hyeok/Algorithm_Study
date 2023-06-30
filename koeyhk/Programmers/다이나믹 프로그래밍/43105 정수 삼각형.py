# Bottom-Up
# 작은 문제부터 차근차근 답을 도출하는 방법 - 직관적 (DP의 전형적인 형태)
def solution(triangle):
    d = [[0] * i for i in range(1, len(triangle) + 1)]
    for i in range(len(triangle)-1, -1, -1):
        for j in range(len(triangle[i])):
            if i == len(triangle) - 1:      # 삼각형 바닥의 숫자일 경우
                d[i][j] = triangle[i][j]
            else:
                d[i][j] = max(d[i+1][j], d[i+1][j+1]) + triangle[i][j]
    return d[0][0]

# Top-Down
# 큰 문제를 해결하기 위해 작은 문제 호출
# 코드가 상대적으로 깔끔하지 않음

def solution(triangle):
    d = [[0] * i for i in range(1, len(triangle) + 1)]
    d[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if 0 < j:                       # 맨 왼쪽의 숫자가 아니라면
                d[i][j] = triangle[i][j] + d[i - 1][j - 1]
            if j < len(triangle[i])-1:      # 맨 오른쪽의 숫자가 아니라면
                d[i][j] = max(d[i][j], triangle[i][j] + d[i - 1][j])
    return max(d[len(triangle)-1])          # DP의 마지막 원소들 중 최댓값