print('niger')

print('cyka')

x = 76

n = int(input())
for i in range(n):
    s = input()
    if s == '' or s.isspace():
        print(f'{i+1}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i+1}: {s}')

s = input()
c = 0
for i in s:
    if i in 'qwertyuiopasdfghjklzxcvbnm' or i in '0123456789':
        c += 1
if s[0] == '@' and 5 <= len(s) <= 15 and c == len(s)-1:
    print('Correct')
else:
    print('Incorrect')
