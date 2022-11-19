a = 'hello hello Hello hello'
counter = 0
for i in range(len(a)-2):
    if a[i]+a[i+1]+a[i+2] == 'hel':
        counter+=1
    if counter == 2:
        print(i+1)
        break
