import sys
from itertools import combinations, permutations
input = sys.stdin.readline

"""
조합 경우의 수를 모두 구하고 
다 더해서 S 와 일치하면 cnt +1
"""

n, s = map(int, input().split())
li = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    x = list(combinations(li, i))

    for d in x:
        if sum(d) == s:
            cnt += 1
print(cnt)

# dfs 로 구현

# def dfs(idx, num):
#     global cnt
#     if idx >= n:
#         return
#     num += s_[idx]
#     if num == s:
#         cnt += 1
#     dfs(idx + 1, num - s_[idx])
#     dfs(idx+1, num)


# n, s = map(int, input().split())
# s_ = list(map(int, input().split()))
# cnt = 0
# dfs(0, 0)
# print(cnt)
