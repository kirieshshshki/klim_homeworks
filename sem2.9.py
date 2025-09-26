a = list(input())
c = 0
for i in range(len(a)):
    if a[i] == ' ':
        if a[i-1] == '.' or a[i-1] == ':' or a[i-1] == ';' or a[i-1] == '!' or a[i-1] == '?':
            c += 1
print(c+1)