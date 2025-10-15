test = str(input("Введите текст:"))
with open('Text File(1).txt', 'w', encoding="utf-8") as file:
    file.write(test)

print("Ваш текст успешно сохранен в файл")