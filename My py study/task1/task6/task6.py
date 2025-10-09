def parse(x):
    try:
        return int(x)
    except ValueError:
        return x


def summa(a,b):
    
    return a+b

sum1 = parse(input("Введіть 1 значення: "))
sum2 = parse(input("Введіть 2 значення: "))
result = summa(sum1,sum2)

print(sum1, "+", sum2, "=", result)