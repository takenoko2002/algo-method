
N = int(input())

A = []

for i in range(1,N+1):
    A.append(i)

i = 0
while len(A) > 1:
    if i % 2 == 0:
        A.pop(0)
    else:
        #取り出して末尾に追加
        A.append(A.pop(0))
    i += 1

print(A.pop(0))