from bisect import bisect_right, bisect_left
from collections import defaultdict


def count_by_range(a, left_value, right_value):     # 특정 범위에 속하는 데이터 개수 구하기
    return bisect_right(a, right_value) - bisect_left(a, left_value)


def solution(words, queries):
    answer = []
    # 나온 적 없는 키로 접근이 가능하도록 defaultdict() 사용
    w, rw = defaultdict(list), defaultdict(list)

    # 단어들을 길이에 따라 순서대로, 반대로 저장
    for word in words:
        w[len(word)].append(word)
        rw[len(word)].append(word[::-1])

    # 해당 길이의 단어들을 순서대로 정렬
    for l in w.values():
        l.sort()
    for l in rw.values():
        l.sort()

    # queries 탐색
    for query in queries:
        if query[0] == '?':     # ?로 시작하는 키워드라면
            # 키워드를 뒤집어 start에 ?를 'a'로 바꿔 저장, end에 ?를 'z'로 바꿔 저장
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
            # 키워드의 길이와 동일한 뒤집은 단어들 중 start와 end 사이의 단어 개수를 더해 저장
            answer.append(count_by_range(rw[len(query)], start, end))
        else:                   # ?로 시작하는 키워드가 아니라면
            # 키워드에서 start에 ?를 'a'로 바꿔 저장, end에 ?를 'z'로 바꿔 저장
            start, end = query.replace('?', 'a'), query.replace('?', 'z')
            # 키워드의 길이와 동일한 단어들 중 start와 end 사이의 단어 개수를 더해 저장
            answer.append(count_by_range(w[len(query)], start, end))
    return answer


# 딕셔너리에 대한 정리 필요!
# 단어를 비교하기 위해 생각했던 아이디어
# 1. split('?')
# 2. 사전 순 정렬 후 이진 탐색하며 범위 찾기
# 3. str.startswith(문자열), str.endswith(문자열)