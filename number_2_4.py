def describe_person(name, age=30):
    return f'Имя: {name}, возраст: {age}'
name = str(input("Введите ваше имя: "))
print(describe_person(name))