#途中
N = int(input())

A = []

for i in range(1,N+1):
    A.append(i)

i = 0
pre_lenA = len(A)
while len(A) > 1:
    if i >= len(A):
        if pre_lenA % 2 == 0 or len(A) == 3:
            i = 0
        else:
            i = 1
        pre_lenA = len(A)
    A.pop(i)
    i += 1

print(A.pop(0))
