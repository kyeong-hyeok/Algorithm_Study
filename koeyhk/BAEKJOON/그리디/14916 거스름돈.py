n = int(input())
p=1
for i in range(n//5, -1, -1):
    k=n-5*i
    if k%2==0:
        p=0
        print(k//2+i)
        break
if p:
    print(-1)