def filtered(obj: list, lam):
    re = []
    for i in range(len(obj)):
        if lam(obj[i]) is True:
            re.append(obj[i])  # 这里有修改
    return re


if __name__ == '__main__':
    items = [i for i in range(101)]
    mul_3 = filtered(items, lambda x: x % 3 == 0)
    print(', '.join([str(x) for x in mul_3]))  # 修改
    mul_5 = filtered(items, lambda x: x % 5 == 0)
    print(', '.join([str(x) for x in mul_5]))  # 修改
    mul_15 = filtered(items, lambda x: x % 15 == 0)
    print(', '.join([str(x) for x in mul_15]))  # 修改

# 这是提交之后参考别人答案修改的，checker判定正确
# 下面是我最最原本的答案，checker判定错误，我不明白这两种有什么区别，错误提示的截图放在邮件中
# 17. Lambda expressions.py中的最终答案输出的函数显得有些繁琐，是在下面代码输出不符合要求后修改得到的


def filtered(obj: list, lam):
    re = []
    for i in range(len(obj)):
        if lam(obj[i]) is True:
            re.append(str(obj[i]))
    return re


if __name__ == '__main__':
    items = [i for i in range(101)]
    mul_3 = filtered(items, lambda x: x % 3 == 0)
    print(', '.join(mul_3))
    mul_5 = filtered(items, lambda x: x % 5 == 0)
    print(', '.join(mul_5))
    mul_15 = filtered(items, lambda x: x % 15 == 0)
    print(', '.join(mul_15))