import sys

n = int(input())
for _ in range(n):
    A, B = map(int, sys.stdin.readline().strip().split())
    print(A + B)