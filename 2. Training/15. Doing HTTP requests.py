import requests
try:
    x = requests.get('https://api.github.com/users/python')
    print(x.text)
# 错误类型是从网站上别人做的答案抄来的，最开始没有写错误类型
except requests.ConnectionError:
    print('No internet connectivity.')
