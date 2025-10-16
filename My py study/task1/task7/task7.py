#Завдання 1
text = input("Введіть текст для занесення в файл: ")

file = open("text.txt", "a")
file.write(text + "\n")
file.close()

#Завдання 2
file = open("text.txt", "r")
# print(file.read())
for line in file:
    print(line, end="")
file.close()