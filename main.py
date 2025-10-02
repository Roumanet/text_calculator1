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

