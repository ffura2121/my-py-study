step1 = {"folder1": "Документи", "folder2": "Роб.Стіл", "folder3": "Ігри"}
step2 = {"Документи": "Немає файлів", "Роб.Стіл": "Корзина", "Ігри": "Steam"}
print("Наявні ключі: ", list(step1.keys()))
answer = input("Обери папку (1-3): ")
answer_folder = "folder"+answer
if answer_folder in step1:
    print(step2[step1[answer_folder]])
else:
    print("Такої папки немає")