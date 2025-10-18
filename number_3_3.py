try:
    with open('Text File (2).txt', 'r', encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не существует")