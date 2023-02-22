# 4:11 - 4:19

# 연속된 1덩어리 수와 0덩어리 수를 세어, 더 작은 수를 반환

arr = input()
cnt1 = 0
cnt0 = 0


for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
        if arr[i-1] == '0':
            cnt0 += 1
        else:
            cnt1 += 1


# 앞, 뒤를 비교해서 다르면 앞의 cnt만 올려줘서, 마지막 것은 뒤가 없으니까 cnt가 안올라감.
# 그래서 맨 뒤 값 확인 후, cnt 올려주기
if arr[-1] == '0':
    cnt0 += 1
else:
    cnt1 += 1

print(min(cnt0, cnt1))
