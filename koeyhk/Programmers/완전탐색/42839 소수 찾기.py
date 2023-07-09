from itertools import permutations


def solution(numbers):
    dic = {}
    num = list(numbers)     # numbers를 나누어 list로 저장
    for i in range(1, len(num)+1):  # num의 원소들로 순열을 만들기 위한 for 문
        perm = list(permutations(num, i))   # 순열 만들기
        for p in perm:      # 순열의 원소들에 돌아가는 for 문
            a = ''
            for n in p:     # 순열의 원소 합치기
                a += n
            s = 1           # 소수 여부 확인하기 위한 변수
            for k in range(2, int(int(a)**0.5) + 1):    # 제곱근보다 작은 숫자까지 나눗셈
                if int(a) % k == 0:
                    s = 0
                    break
            if s == 1 and int(a) > 1 and int(a) not in dic:     # 소수이고 1보다 크고 dic에 같은 값이 없을 경우
                dic[int(a)] = 1     # dic에 저장
    return len(dic)