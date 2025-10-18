test = str(input("Введите текст:"))
with open('Text File(1).txt', 'w', encoding="utf-8") as file:
    file.write(test)

print("\nВаш текст успешно сохранен в файл")
