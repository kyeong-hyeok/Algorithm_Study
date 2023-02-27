# 11:34 - 12:20

# 내가 푼 풀이
def solution(_str):
    length = len(_str)
    if length == 1:
        return 1

    answer = 1000
    for i in range(1, (length // 2) + 1):
        total_sum = 0
        _sum = 1
        for j in range(0, length, i):
            if j + 2 * i > length: # 비교할 다음 대상이 없는 경우
                if _sum == 1: # 앞 부분과 같지 않은 경우
                    total_sum += len(_str[j:]) # 나머지 문자열의 길이를 더해줌
                else: # 앞 부분과 같은 경우
                    if _str[j:j + i] == _str[j + i:]: # 현재 부분과 다음 남은 부분이 같은 경우
                        _sum += 1
                        total_sum += (i + len(str(_sum)))
                    else: # 다른 경우
                        total_sum += (i + len(str(_sum)))
                        total_sum += len(_str[j + i:])
                break

            if _str[j:j + i] == _str[j + i:j + 2 * i]:
                _sum += 1
            else:
                if _sum == 1:
                    total_sum += i
                else:
                    total_sum += (i + len(str(_sum)))
                _sum = 1

        answer = min(total_sum, answer)
    return answer

# 다른 사람 풀이
def solution(s):
    result = []
    if len(s) == 1:
        return 1

    for i in range(1, (len(s)//2) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s), i):
            if tmp == s[j:i+j]: # 같은 경우
                cnt += 1
            else: # 다른 경우
                if cnt != 1: # 이전에 같은 경우가 존재했던 경우
                    b = b + str(cnt) + tmp
                else: # 이전에 같은 경우가 존재하지 않았던 경우
                    b = b + tmp
                tmp = s[j:j+i] # 다음 비교 대상 문자열 변경
                cnt = 1 # 개수 초기화

        # 마지막 부분 처리
        if cnt != 1: # 이전 것과 같았다면
            b = b + str(cnt) + tmp
        else: # 이전 것과 같지 않았다면
            b = b + tmp

        result.append(len(b)) # result에는 길이 별로 압축된 문자열의 길이 저장
    return min(result)