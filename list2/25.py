def format(a):
    b = ''
    c = a[::-1]
    for i in range(len(c)):
        b+=a[i]
        b+='-'
    for i in range(len(a)):
        b+=a[i]
        b+='-'
    return b[:-1]

a = ['val1','val2','val3']
print(format(a))