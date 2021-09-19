A = [int(i) for i in input().split()]
k = 0
for (i, A) in enumerate(range(len(A))):
    print(i, A[i])
    if A[i] == 0:
        A.append(A[i])
        A.pop(i)
print(A)