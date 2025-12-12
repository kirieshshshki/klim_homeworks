a = list(input())
s = []
for i in range(len(a)):
    if a.count(a[i]) == 1:
        s.append(a[i])
print(' '.join(s))