# ввод a, b
a = int(input())
b = int(input())

# проверка на нули
if a == 0 and b == 0:
    print('INF')
elif a == 0 or (b % a) != 0: # условие когда нет корней
    print('NO')
else:
    print(-b // a)