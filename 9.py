winter = ['december','january','february']
spring = ['march','april','may']
summer = ['june','july','august']
autumn = ['september','october','november']
months = {1:'january',2:'february',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
length = {'january':31,'february':29,'march':31,'april':30,'may':31,'june':30,'july':31,'august':31,'september':30,'october':31,'november':30,'december':31}
print('Введите день')
day = int(input())
print('Введите месяц')
month = int(input())
print('Введите год')
year = int(input())
if (day >31 and day<1) or (month>12 or month<1):
    print('написана ересь')
elif day > length.get(months[month]):
    print('Такой даты не существует')
if day <= length.get(months[month]) and day>0:
    if months.get(month) in winter:
        print('winter')
    if months.get(month) in spring:
        print('spring')
    if months.get(month) in summer:
        print('summer')
    if months.get(month) in autumn:
        print(autumn)

