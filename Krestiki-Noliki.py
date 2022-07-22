P1 = [" ", 1, 2, 3]
P2 = [1, "-", "-", "-"]
P3 = [2, "-", "-", "-"]
P4 = [3, "-", "-", "-"]
Matrix = [P1, P2, P3, P4]

list_cancel = []
check_list = ["1.1", "1.2", "1.3", "2.1", "2.2", "2.3", "3.1", "3.2", "3.3"]
H1 = "x"
H2 = "o"
HA = H1

while True:
    print(" ", *P1, "\n", *P2, "\n", *P3, "\n", *P4)
    L = input(f"Игрок {HA} Ваш ход")
    if L not in check_list:
        print("Вы должны указать координаты вашего хода через точку в формате x.y")
        continue
    else:
        if L in list_cancel:
            print("Эта клетка уже занята")
        else:
            list_cancel.append(L)
            Matrix[int(L[0])][int(L[2])] = HA
            if HA == H1:
                HA = H2
            else:
                HA = H1
    if any([list(P2[1:4]) == ["x", "x", "x"],
            list(P2[1:4]) == ["o", "o", "o"],
            list(P3[1:4]) == ["x", "x", "x"],
            list(P4[1:4]) == ["x", "x", "x"],
            list(P4[1:4]) == ["o", "o", "o"],
            all([P2[1] == "x",
                 P3[1] == "x",
                 P4[1] == "x"]),
            all([P2[2] == "x",
                 P3[2] == "x",
                 P4[2] == "x"]),
            all([P2[3] == "x",
                 P3[3] == "x",
                 P4[3] == "x"]),
            all([P2[1] == "o",
                 P3[1] == "o",
                 P4[1] == "o"]),
            all([P2[2] == "o",
                 P3[2] == "o",
                 P4[2] == "o"]),
            all([P2[3] == "o",
                 P3[3] == "o",
                 P4[3] == "o"]),
            all([P2[1] == "x",
                 P3[2] == "x",
                 P4[3] == "x"]),
            all([P2[3] == "x",
                 P3[2] == "x",
                 P4[1] == "x"]),
            all([P2[1] == "o",
                 P3[2] == "o",
                 P4[3] == "o"]),
            all([P2[3] == "o",
                 P3[2] == "o",
                 P4[1] == "o"]),
            list(P3[1:4]) == ["o", "o", "o"]]):
        print(" ", *P1, "\n", *P2, "\n", *P3, "\n", *P4)
        print(f"Конец игры, игрок {HA} проиграл")
        break
    else:
        if all(["-" not in P2,
                "-" not in P3,
                "-" not in P4]):
            print(" ", *P1, "\n", *P2, "\n", *P3, "\n", *P4)
            print("Ничья")
            break
        else:
            continue
