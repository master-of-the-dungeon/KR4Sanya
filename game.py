

game_field = [['-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-']]  # поле 1

new_field = [['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-']] #поле 2

marks = {}
max_moves = 19
game_status = True
biggest = 100


def str_pnt(): #начальное положение
    while True:
        strpot = int(input('Введите номер строки: '))
        if strpot > 4 or strpot < 1:
            print('Неверная координата строки, введите еще раз')
        else:
            return strpot


def clmn_pnt():
    while True:
        clmnpot = int(input('Введите номер столбца: '))
        if clmnpot > 5 or clmnpot < 1:
            print('Неверная координата столбца, введите еще раз')
        else:
            return clmnpot


def gm_statement(n):  # проверка оставшихся ходов
    if n <= 0:
        return False
    return True


def counting_points(wide_matrix, x, y, number):
    mtrix = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            mtrix.append(wide_matrix[i][j])
    # print(mtrix)
    if mtrix.count(number) > 1:
        '''
        print('True')
        print(marks[str(number)])
        '''
        marks[str(number)] += 1


'''



Основная игра



'''

while game_status == True:

    while True:
        string_point = str_pnt()
        column_point = clmn_pnt()
        player_number = str(input('введите номер игрока: '))
        if game_field[string_point - 1][column_point - 1] == '-':  # проверка на заполнение
            break
        else:
            print('Эта точка уже занята, попробуйте другую')

    game_field[string_point - 1][column_point - 1] = player_number  # changing point to player symbol
    new_field[string_point][column_point] = player_number   # adding point to bigger field

    marks[str(player_number)] = marks.get(str(player_number), 0)    # adding mark of player

    counting_points(new_field, string_point, column_point, player_number)   # after game move checking penalty pnts

    max_moves -= 1  # changing max moves

    print('  1 2 3 4 5')
    kkk = 1
    for i in game_field:  # output of game field
        print(f'{kkk} ', end = '')
        kkk += 1
        for j in i:
            print(j, end=' ')
        print(end='\n')
    #print(f'Очки: {marks}')

    game_status = gm_statement(max_moves)  # changing game status to false


'''



Время подсчета очков




'''

print(marks)

winners = {}
for i in marks:
    if marks[i] < biggest:
        biggest = marks[i]
        winners.clear()
        winners[i] = marks[i]
    elif marks[i] == biggest:
        winners[i] = marks[i]

print('Winners')
for j in winners:
    print( j, end = ' ')
print(f'with lowest mark: {biggest}')


