with open('words.txt') as words:
    n = 0
    for i in words.read():
        if i == 'e':
            n += 1
    print(n)
