A, B = map(int, input().split())
cnt = 0
while A != B:
    if B % 10 == 1 and B // 10 >= A:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        cnt = -2
        break
    cnt += 1
print(cnt+1)