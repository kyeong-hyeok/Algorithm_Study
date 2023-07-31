from collections import deque


def solution(numbers, target):
    minus_numbers = []
    for n in numbers:
        minus_numbers.append(-n)
    q = deque()
    q.append((numbers[0], 0))
    q.append((minus_numbers[0], 0))
    result = 0
    while q:
        n, inx = q.popleft()
        if inx == len(numbers)-1:
            if n == target:
                result += 1
            continue
        q.append((n + numbers[inx+1], inx+1))
        q.append((n + minus_numbers[inx+1], inx+1))
    return result