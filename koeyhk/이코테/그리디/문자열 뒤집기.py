# 풀이 1
S = input()
l = len(S)
cnt = 0
for i in range(l-1):
    if S[i] != S[i+1]:
        cnt += 1
if cnt % 2 != 0:
    cnt += 1
print(cnt//2)

# 풀이 2
# S = input()
# print(max(S.count('01'), S.count('10')))

# 풀이 3
# S = input()
# S1 = S
# cnt1 = 0
# l = len(S)
# for i in range(l):
#     if S1[i] == '0' and (i+1 == l or S1[i+1] != '0'):
#       cnt1 += 1
# cnt2 = 0
# for i in range(l):
#     if S[i] == '1' and (i+1 == l or S[i+1] != '1'):
#         cnt2 += 1
# print(min(cnt1, cnt2))