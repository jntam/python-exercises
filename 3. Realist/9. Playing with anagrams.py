import string
import unicodedata


def standardizing(words: any):
    # 去除标点符号、音符标记
    words = unicodedata.normalize('NFD', words)
    words = ''.join(c for c in words if not unicodedata.combining(c))
    # 去除空格、统一小写
    words = "".join(w for w in words if w not in string.punctuation)
    words = words.replace(' ', '').lower()

    letter_list = sorted(list(words))
    return letter_list


def is_anagram(left, right):
    if standardizing(left) == standardizing(right):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_anagram('Madam Curie', 'Radium came'))
