x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x_res = x1 - x2
y_res = y1 - y2

if abs(x_res) > 1 or abs(y_res):
    print('NO')
else:
    print('YES')
