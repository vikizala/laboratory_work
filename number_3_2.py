with open('Text File.txt', 'r') as file:
    for line in file:
        print(line.strip())
        # print(line.split('.')[0])
    # print(file.read(90))
    # content = file.read()
    # words = content.split()
    # print(','.join(words))