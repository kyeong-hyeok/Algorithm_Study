# 못품

# 12:33 - 12:51

# 요약
# n종류 당근 t일동안 재배
# 처음에는 wi의 맛을 가짐
# 오리 : 매일 i자리에 당근 없으면 당근 심고, 있다면 pi만큼 당근의 맛을 올리는 영양제 줌
# 토끼 : 하루에 최대 하나의 당근 먹을 수 있음
# 토끼가 먹은 당근의 맛의 합의 최댓값

# idea
# 항상 w<=p
# 당근 종류가 1개일 때를 생각해도, 어짜피 w<=p라서 p가 최소인 w=p일 때도, 매일 뽑고 다시심는것 = 기다렸다가 마지막 날 뽑는것


n, t = map(int, input().split())
carrots = [list(map(int, input().split())) for _ in range(n)]
carrots.sort(key = lambda x: x[1]) # 매일 증가하는 양 기준으로 오름차순 정렬

result = 0
feeded_days = t-n
for w, p in carrots:
    result += (w + p * feeded_days)
    feeded_days += 1

print(result)