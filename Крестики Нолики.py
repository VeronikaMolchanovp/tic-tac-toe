def greet():
    print("--------")
    print("Приветствуем вас")
    print("в игре")
    print("крестики нолики")
    print("--------")
    print("формат ввода: x y")
    print("x- номер строки")
    print("y- номер столбца")

field = [[" "]*3 for i in range(3)]
def snow_field():
    print()
    print("   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(map(str,row))} | "
        print(row_str)
        print("----------------")
    print()
def ask():
    while True:
        cords =input("Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue

        x,y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x,y = int(x),int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] ==" ":
                return x,y
            else:
                print("Клетка зянята!")
        else:
            print("Координаты вне диапозона!")

def check_win():
    win_cords = [((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
                 ((0,2),(1,1),(2,0)),((0,0),(1,1),(2,2)),((0,0),(1,0),(2,0)),
                 ((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2))]
    for cord in win_cords:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print(f"Выиграл {field[a[0]][a[1]]}!")
            return True
    return False
greet()
account = 0
while True:
    account += 1

    snow_field()

    if account % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x,y = ask()

    if account % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        snow_field()
        check_win()
        break

    if account == 9:
        snow_field()
        print("Ничья")
        break