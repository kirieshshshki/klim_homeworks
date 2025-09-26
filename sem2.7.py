a = list(map(int, input().split()))
b = [0] * (max(a) + 1)
for i in range(len(a)):
    b[a[i]] += 1
print(b.index(max(b)))