# 6:25 - 6:35

# idea
# 완성본에서 거꾸로 거슬러오기
# 2를 나누는 것보다 수의 끝의 1을 없애는 것이 더 연산 속도적으로 빠름

a, b = map(int, input().split())

answer = 1
while b != a:
    if b == 1: # 무한루프 방지
        answer = -1
        break

    if b % 10 == 1:
        b //= 10
        answer += 1
    elif b % 2 == 0:
        b //= 2
        answer += 1
    else:
        answer = -1
        break

print(answer)

# 주의)
# 무한루프에 걸리지 않는지 확인할 것
