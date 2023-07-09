def solution(sizes):
    max_left, max_right = 0, 0      # 가로 최댓값, 세로 최댓값
    for s in sizes:
        max_left = max(max_left, max(s))    # 명함의 가로 - max(s)
        max_right = max(max_right, min(s))  # 명함의 세로 - min(s)
    return max_left * max_right