values = 'hello hello Hello hello'.split()
val2 = ''
for count, value in enumerate(values):
     val2 +=value
     val2+=str(count+1)
print(val2)