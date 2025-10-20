#Задача №1
qq = True
while qq:
    try:
        num = int(input("Введіть будь-яке число: "))
        num_in_2 = num * num
        print("Ви ввели число", num, "\nКвадрат числа",num,"=",num_in_2)
        qq = False
    except ValueError:
        print("Введіть саме число, повторіть свою спробу знову:")

#Задача №2
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))

try:
    resultat = number1//number2
    print(number1,":",number2,"=",resultat)
except ZeroDivisionError:
    print("Ділення на нуль неможливе!")

#Задача №3
znachenya1 = input("Введіть число: (1/5) ")
znachenya2 = input("Введіть число: (2/5) ")
znachenya3 = input("Введіть число: (3/5) ")
znachenya4 = input("Введіть число: (4/5) ")
znachenya5 = input("Введіть число: (5/5) ")

suma = 0
suma_list= [znachenya1, znachenya2, znachenya3, znachenya4, znachenya5]
skipped = []

for el in suma_list:
    try:
        suma += float(el)
    except ValueError:
        skipped.append(el)

print("Сума чисел =", suma)
print("Те що не являється числом, та не могло сумуватися:",skipped)
