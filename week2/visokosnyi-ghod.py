number = int(input())

if ((number % 4 == 0) and (number % 100 != 0)) or (number % 400 == 0):
    print('YES')
else:
    print('NO')
