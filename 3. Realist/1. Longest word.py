import string


def longest_word(text: str):
    length: int = 0
    longest: str = ""
    text = "".join(w for w in text if w not in string.punctuation)      # 去标点
    # print(text)
    _text = text.split()        # sep默认值是以连续的<空格>、<换行符>、<制表符>作为分割符
    # print(_text)
    for word in _text:
        if len(word) > length:
            length = len(word)
            longest = word
    return longest


if __name__ == '__main__':
    print(longest_word("We want\na SHRUBBERY"))