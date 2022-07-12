from datetime import datetime as d

present_time = d.now()
print('Today is ' + str(present_time.date()) + ' and it is '
      + str(present_time.time().replace(microsecond=0)) + '.')


# -----------
now = d.now()
# print("Today is {} and it is {}."
#       .format(now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")))
print(now.strftime("Today is %Y-%m-%d and it is %H:%M:%S."))
