# 풀이 1 - 집합 (순서 x, 중복 x)
def solution(nums):
    return min(len(set(nums)), len(nums)//2)

# 풀이 2 - 딕셔너리
def solution(nums):
    d = {}
    for n in nums:
        d[n] = 1
    if len(nums) / 2 < len(d):
        return int(len(nums) / 2)
    else:
        return len(d)