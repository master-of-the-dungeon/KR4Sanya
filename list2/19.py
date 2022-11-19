a = 'Hello world'
c = []
b = ''
for i in range(len(a)):
    c.append(a[i])
for i in range(len(c)):
    b+=c[i]
    b+='->'
print(b)