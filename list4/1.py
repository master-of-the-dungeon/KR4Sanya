a = 'aaaahjhdsfjkdsbsaeeepxdvbdnsafdew'
b = 'dbsafewvbfsadgqwebDVapdsf'
c = ''
for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j] and b[i] not in c:
            c+=b[i]
print(c)