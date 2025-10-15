text = str(input("Введите текст: "))
with open('Text File.txt', 'a', encoding="utf-8") as file:
    end_text = file.write(text)
print(end_text)