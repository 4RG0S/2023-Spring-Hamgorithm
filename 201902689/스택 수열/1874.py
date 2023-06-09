import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

stack = []
result = []
now = 1
isTrue = True
for num in nums:
    while now <= num:
        stack.append(now)
        result.append('+')
        now += 1
    tmp = stack.pop()
    if tmp == num:
        result.append('-')
    else:
        print("NO")
        isTrue = False
        break

if isTrue:
    for txt in result:
        print(txt)