the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]
# 原答案   若元素数变化可以将range(10)改为range(len(the_list))
# n = the_list[0]
# for i in range(10):
#    if n < the_list[i]:
#        n = the_list[i]

max_value = max(the_list)
print(max_value)
