import re
a = 'aaa--bbb==ccc__ddd'
a = re.split('--|==|__', a)
print(a)

