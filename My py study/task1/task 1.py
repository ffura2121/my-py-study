n = int(input("Введіть довжину: "))
user_list = []

i = 0
while i < n:
    string = int(input("Додати елемент №" + str(i+1) + ": "))
    user_list.append(string)
    i += 1
user_list.sort()
print((user_list))