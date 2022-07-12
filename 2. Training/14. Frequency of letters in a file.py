import string

with open('words.txt') as words:
    freq = {}
    obj = str(words.read().lower())

    # 唱票
    for i in obj:
        # 跳过非字母
        if i not in string.ascii_lowercase:
            continue
        if i not in freq:
            freq[i] = 0
        # if i in freq.keys(): 多余//freq.keys() =>freq
        freq[i] += 1

    # 打印
    for i in freq.keys():
        print("{}: {:.2f}".format(i, freq[i]/len(obj)))
# 修改
