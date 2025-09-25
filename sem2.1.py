'''list1 = ['E', 'J', 'S', 'Z']
list2 = ['3', 'L', '2', '5']
list3 = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
a = list(input())
per1 = 0
per2 = 0
for i in range(len(a)//2+1):
    if a[i] == a[-i-1]:
        if a[i] in list3:
            per1 += 1
    elif list1.index(input(a[i])) == list2.index(input(a[-i-1])) or list2.index(input(a[i])) == list1.index(input(a[-i-1])):
        per2 += 1
    else:
        print(''.join(a), ' is not a palindrome')
        per2 = -1
        break
if per1 == len(a)//2+1:
    print(''.join(a), ' is a mirrored palindrome')
elif per1 > 0 and per2 == 0:
    print(''.join(a), ' is a regular palindrome')
elif per2 != -1:
    print(''.join(a), ' is a mirrored string')'''

list1 = ['E', 'J', 'S', 'Z']
list2 = ['3', 'L', '2', '5']
list3 = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']

a = list(input())
per1 = 1
per2 = 1

for i in range(len(a)//2+1):
    if a[i] != a[-i-1]:
        per1 = 0
        per2 = 0
        print(''.join(a), 'is not a palindrome.')
        break
    if a[i] in list3:
        if a[i] != a[-i-1]:
            per2 = 0
    elif a[i] in list1:
        if list2.index(a[-i-1]) != list1.index(a[i]):
            per2 = 0
    elif a[i] in list2:
        if list1.index(a[-i-1]) != list2.index(a[i]):
            per2 = 0
if per1 == 1 and per2 == 1:
    print(''.join(a), 'is a mirrored palindrome.')
elif per1 == 1:
    print(''.join(a), 'is a regular palindrome.')
elif per2 == 1:
    print(''.join(a), 'is a mirrored string.')