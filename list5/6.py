import re
a = input()
a = re.split('@',a)
if '.' in a[1] and len(a[1])>2:
    print('Все правильно')
else:
    print('Обнаружена ересь, введите правильный мейл')