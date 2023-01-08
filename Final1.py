pole = [[" "] *3 for i in range(3)]
print(pole)

def field():
    print(f"  | 0 | 1 | 2 |")
    print("--------------------")
    print(f"0 | {pole[0][0]} | {pole[0][1]} | {pole[0][2]} |")
    print("--------------------")
    print(f"1 | {pole[1][0]} | {pole[1][1]} | {pole[1][2]} |")
    print("--------------------")
    print(f"2 | {pole[2][0]} | {pole[2][1]} | {pole[2][2]} |")
    print("--------------------")
def vvod():
    while True:
        coord = input("          Ваш ход:").split()
        if len(coord) != 2:
            print(" Введите две координаты ")

            continue
        x, y = coord
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа ")
            continue
        x, y = int(x), int(y)
        if  0  > x or x > 2 or  0 > y  or y > 2:
            print(" Координаты вне диапазона ")
            continue
        if pole[x][y] != " ":
            print(" Клетка занята ")
            continue
        return x, y


nm = 0
while True:
    nm += 1
    field()
    if nm % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")
    x, y = vvod()
    if nm % 2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "0"







