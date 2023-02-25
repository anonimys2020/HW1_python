# ввод x
x = int(input())

tens = x // 10
units = x % 10

# условия для десятков
if tens == 10:
    result = "C"
elif tens == 9:
    result = "XC"
elif tens == 4:
    result = "XL"
elif tens >= 5:
    result = "L" + (tens - 5)*"X"
else:
    result = tens*"X"

# условия для единиц
if units == 9:
    result += "IX"
elif units == 4:
    result += "IV"
elif units >= 5:
    result += "V" + (units - 5)*"I"
else:
    result += units*"I"

# вывод result
print(result)
