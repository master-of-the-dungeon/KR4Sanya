a = 'hello hello Hello hello'
counter = 0
a = a[::-1]

for i in range(len(a)-2):
    if a[i]+a[i+1]+a[i+2] == 'leh':
        counter+=1
    if counter == 2:
        print(i+3)
        break
