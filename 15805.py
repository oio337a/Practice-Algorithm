import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

for i in range(1, n):
    print(li[i])