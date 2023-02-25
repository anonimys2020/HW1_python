# ввод k, n, m
k = int(input()) # котлет за раз
m = int(input()) # минут на прожарку одной стороны
n = int(input()) # всего нужно пожарить котлет

# Проверяем условия
if n <= k:
    print(int(m * 2))
elif ((2 * n) % k) == 0:
    result = (2 * n // k) * m
    print(int(result))
else:
    result = (1 + (2 * n // k)) * m
    print(int(result))