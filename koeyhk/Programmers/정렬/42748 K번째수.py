array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    result = []
    for c in commands:
        i, j, k = c
        ar = array[i-1:j]
        ar.sort()
        result.append(ar[k-1])
    return result

print(solution(array, commands))