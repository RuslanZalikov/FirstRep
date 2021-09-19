a = []
n = int(input())
i = 0
k = 0
for i in range(n):
    a.append(int(input()))
print(a)
a.sort(reverse=True)
print(a)
for (i, e) in enumerate(range(len(a) - 2)):
    if a[i] > 0 and a[i + 1] > 0 and a[i + 2] > 0 and a[i] + a[i + 1] > a[i + 2] and a[i + 2] + a[i + 1] > a[i] and a[i + 2] + a[i] > a[i + 1]:
        print(a[i], a[i + 1], a[i + 2])
        k+=1
        break
if k==False:
    print("Не бывает!")