'''"ABC is not a palindrome."
"ABA is a regular palindrome."
"EA3 is a mirrored string."
"AMA is a mirrored palindrome."
'''

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
        if a[-i-1] != list2[list1.index(a[i])]:
            per2 = 0
    elif a[i] in list2:
        if a[-i-1] != list1[list2.index(a[i])]:
            per2 = 0
    else:
        per2 = 0
        break
if per1 == 1 and per2 == 1:
    print(''.join(a), 'is a mirrored palindrome.')
elif per1 == 1:
    print(''.join(a), 'is a regular palindrome.')
elif per2 == 1:
    print(''.join(a), 'is a mirrored string.')