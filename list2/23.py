a = ' start hello python world'.split()
print(a)
for i in range(len(a)):
    if a[i].startswith('he'):
        for j in range(i,len(a)):
            if a[j].endswith('on'):

                print(a[i],a[j])
                del a[i]
                del a[j-1]
                break
        break
print(a)