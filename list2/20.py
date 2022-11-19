a = '  HeLLO WOrlD'
b = 'hello WORLDdd  '
print(a,b)


if a.lower().strip() == b.lower().strip():
    print('Они одинаковые')
else:
    print('Обнаружена ересь, они разные')