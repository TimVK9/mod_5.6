def hello():
    print()
    print('Добро пожаловать в игру "Крестики нолики!')
    print('Участники по очереди ставят на поле "Х" или "О"')
    print('Каждой клетке соответствует координаты Х и У')
    print('Х - по горизонтали')
    print('У - по вертикали')
    print()
    print('------------------')
    print()


def place():
    print("        0    1    2 ")
    print("        ↓    ↓    ↓ ")
    print()
    for i, row in enumerate(field):
        row = f" {i} →   | {' | '.join(row)} |"
        print(row)
        print()


def insert():
    while True:
        cor = input('Введите координаты: ').split()
        if len(cor) < 2:
            print()
            print('Необходимо ввести два значения!')
            print()
            print('Повторите попытку!')
            continue

        cor_x, cor_y = map(int, cor)
        if 0 < cor_x > 2 or 0 < cor_y > 2:
            print()
            print('Координаты не верные')
            print()
            print('Повторите попытку!')
            continue

        if field[cor_x][cor_y] != "*":
            print()
            print("Такой ход уже был!")
            print()
            print('Повторите попытку!')
            continue

        return cor_x, cor_y


def check():
    win = (((0, 0), (0, 1), (0, 2)),
           ((1, 0), (1, 1), (1, 2)),
           ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)),
           ((0, 0), (1, 1), (2, 2)),
           ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)),
           ((0, 2), (1, 2), (2, 2)))
    for w in win:
        win_str = []
        for i in w:
            win_str.append(field[i[0]][i[1]])
        if win_str == ['x', 'x', 'x']:
            print("Поздравляем! Выиграл X !")
            return True
        if win_str == ['o', 'o', 'o']:
            print('Поздравляем! Выиграл O !')
            return True
    return False


def play():
    step_count = 0
    while True:
        step_count += 1
        place()
        if step_count % 2 == 1:
            print('Ходит "X": ')
        else:
            print('Ходит "O": ')
        x, y = insert()
        if step_count % 2 == 1:
            field[x][y] = 'x'
        else:
            field[x][y] = 'o'
        if check():
            break
        if step_count == 9:
            print("Ничья!")
            break


field = [['*' for row in range(3)] for col in range(3)]

hello()
play()
