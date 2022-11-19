a = 'I Study in FA'
print(len(a))
if len(a)%2==0:
    print(a[int(len(a)/4):int(len(a)-len(a)/4)])
else:
    print('Длина строки нечетная, выводится строка на 1 символ меньше')
    print(a[int(len(a) / 4):int(len(a) - len(a) / 4)])


