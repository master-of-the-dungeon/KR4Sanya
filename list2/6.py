a = input()
if len(a)%2 != 0:
    print(a[int((len(a)/2)-0.5)])
elif len(a)%2==0 and len(a)>2:
    print('длина сторки четная, как таковой середины у нее нет поэтому выводим числа соседние от центра')
    print((a[int((len(a)/2)-1)]))
    print(a[int((len(a) / 2) + 1)])
elif len(a)%2==0 and len(a)<=2:
    print('длина сторки четная, как таковой середины у нее нет поэтому выводим числа соседние от центра')
    print((a[int((len(a) / 2) - 1)]))
