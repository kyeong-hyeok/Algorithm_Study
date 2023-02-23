# 풀이 1
import sys

N = int(input())
num = [int(sys.stdin.readline()) for i in range(N)]
num.sort()
result = 0
i = 0
s = 0   # 0보다 큰 수가 전에 나왔는지 여부
while i < N:  # i가 N보다 작을 때
    if i == N-1:    # i가 N-1이라면 더하고 break
        result += num[i]
        break
    if num[i] > 0 and s == 0:   # 0보다 큰 수가 나오는 첫 번째 수일 때
        num.sort(reverse=True)  # 내림차순 정렬
        s = 1
        N -= i  # N에서 i의 값 만큼 빼고
        i = 0   # i의 값에 0 대입 -> 앞의 인덱스부터 보기 위함
    if num[i] < 0 and num[i+1] <= 0:    # 현재 수가 음수고 다음 수가 0이하일 때
        result += num[i] * num[i+1]     # 묶어야 최대가 됨
        i += 2  # 인덱스 2 증가
    elif num[i] > 1 and num[i+1] > 1:   # 현재 수가 1보다 크고 다음 수가 1보다 클 때
        result += num[i] * num[i+1]     # 묶어야 최대가 됨
        i += 2  # 인덱스 2 증가
    else:
        result += num[i]
        i+=1
print(result)


# 풀이 2
# 풀이 1에서 수를 0보다 큰 수, 0보다 작거나 같은 수로 나누어 보다 직관적인 코드
import sys

N = int(input())
p = []  # 0보다 큰수
m = []  # 0보다 작거나 같은 수
for i in range(N):
    num = int(sys.stdin.readline())
    p.append(num) if num > 0 else m.append(num)     # 0보다 큰 수와 작거나 같은 수로 나누어 저장
m.sort()    # 0보다 작거나 같은 수는 오름차순 정렬
p.sort(reverse=True)    # 0보다 큰 수는 내림차순 정렬
i = 0
ml = len(m)
pl = len(p)
result = 0

while i < ml:   # 0보다 작거나 같은 수에서 돌아가는 while 문
    if i == ml-1:   # 마지막 원소일 경우
        result += m[i]
        break
    result += m[i] * m[i + 1]  # 묶어야 최대가 됨
    i += 2  # 인덱스 2 증가

i = 0
while i < pl:   # 0보다 큰 수에서 돌아가는 while 문
    if i == pl-1:   # 마지막 원소일 경우
        result += p[i]
        break
    if p[i] > 1 and p[i + 1] > 1:  # 현재 수가 1보다 크고 다음 수가 1보다 클 때
        result += p[i] * p[i + 1]  # 묶어야 최대가 됨
        i += 2  # 인덱스 2 증가
    else:   # 그렇지 않으면
        result += p[i]  # 현재 수 하나 더하기
        i += 1
print(result)
