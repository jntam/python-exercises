import unicodedata

for i in range(230000):
    if 'HEART' in unicodedata.name(chr(i), 'name'):
        print(chr(i))
