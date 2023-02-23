# 5:59 - 6:14

# 요약
# 팁 = 원래 주려고 했던 돈 - (받은 등수 - 1)
# 손님의 순서를 적절히 바꿔서, 강호가 받을 수 있는 팁의 최댓값 구하기
# 팁이 음수라면 0원

# idea
# 원래 주려고 했던 돈이 많은 순서대로 서 있는게 최적의 상황

n = int(input()) # 서 있는 사람 수
arr = [int(input()) for _ in range(n)] # 원래 주려고 했던 돈

arr.sort(reverse=True) # 역순 정렬

answer = 0
for i in range(n):
    tip = arr[i] - i # arr[i] - ((i + 1) - 1)
    if tip <= 0: # 팁이 음수라면 더하지 않음
        break # 이 뒤로는 계속 tip이 음수 값이 나올 것이라서 break

    answer += tip

print(answer)
