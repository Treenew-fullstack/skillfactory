import sys #Импортирую модуль для использования exit()
print("Давай сыграем в игру пятнашки?!")

#Цикл для предоставления выбора пользователю символа для игры с фильтром от ошибочных вводов
while "" or True:
    user_choice = input("Каким символом будете играть 'x' или '0'? Введите символ: ")
    if  user_choice == "x":
        pc_symbol = "0"
        print(f"Окей! Ты играешь {user_choice}")
        break
    elif user_choice == "0":
        pc_symbol = "x"
        print(f"Окей! Ты играешь {user_choice}")
        break
    else:
        print(f"Что-то введено не верно... Давайте попробуем ещё раз?! ")
#Игровое поле
list_1 = [" ", "0", "1", "2"]
list_2 = ["0", "-", "-", "-"]
list_3 = ["1", "-", "-", "-"]
list_4 = ["2", "-", "-", "-"]

#Объяснения правил игроку
print(f"Тепеть о правилах!!! Игровое поле состоит из трёх столбцов и трёх строк. Они пронумерованы!  \n"
      f"{("    ").join(list_1)}\n{("    ").join(list_2)}\n{("    ").join(list_3)}\n{("    ").join(list_4)} \n"
      "Сперва Вам предоставится выбор номера столбца, а затем номера строки. \n"
      "После осуществления выбора игровое поле обновится и, выбраный вами символ, \nпоявится на перекрестье" 
      " выбраных вами номеров столбца и строки. После - ход за мной)")

#Функция для проверки алгоритмов победы и завершения программы
def check_win():
    if (list_4[1] == list_4[2] == list_4[3] == "x" or list_3[1] == list_3[2] == list_3[3] == "x" or list_2[1] == list_2[2] == list_2[3] == "x" or
         list_2[1] == list_3[1] == list_4[1] == "x" or list_2[2] == list_3[2] == list_4[2] == "x" or list_2[3] == list_3[3] == list_4[3] == "x" or
         list_2[3] == list_3[2] == list_4[1] == "x" or list_2[1] == list_3[2] == list_4[3] == "x"):
        print("\n \n ПОБЕДИЛ  'Х' ! \n \n")
        print(f"{("    ").join(list_1)}\n{("    ").join(list_2)}\n{("    ").join(list_3)}\n{("    ").join(list_4)} \n")
        sys.exit()
    elif (list_4[1] == list_4[2] == list_4[3] == "0" or list_3[1] == list_3[2] == list_3[3] == "0" or list_2[1] == list_2[2] == list_2[3] == "0"
          or list_2[1] == list_3[1] == list_4[1] == "0" or list_2[2] == list_3[2] == list_4[2] == "0" or list_2[3] == list_3[3] == list_4[3] == "0"
          or list_2[3] == list_3[2] == list_4[1] == "0" or list_2[1] == list_3[2] == list_4[3] == "0"):
        print("\n \n ПОБЕДИЛ  '0' ! \n \n")
        print(f"{("    ").join(list_1)}\n{("    ").join(list_2)}\n{("    ").join(list_3)}\n{("    ").join(list_4)} \n")
        sys.exit()

#Игровой цикл с ходами игрока и компьютера с фильтром от недействительного ввода
while True:
    col_pol = int(input("Введите цифру с номером столбца: "))
    str_pol = int(input("Введите цифру с номером строки: "))
    if col_pol == 0 and str_pol == 0 and list_2[1] == "-":
        list_2[1] = user_choice
        check_win()
        for i in list_2:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_4[list_4.index(i)] = pc_symbol
                break
    elif col_pol == 0 and str_pol == 1 and list_3[1] == "-":
        list_3[1] = user_choice
        check_win()
        for i in list_3:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_2[list_2.index(i)] = pc_symbol
                break
    elif col_pol == 0 and str_pol == 2 and list_4[1] == "-":
        list_4[1] = user_choice
        check_win()
        for i in list_4:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_3[list_3.index(i)] = pc_symbol
                break
    elif col_pol == 1 and str_pol == 0 and list_2[2] == "-":
        list_2[2] = user_choice
        check_win()
        for i in list_2:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_3[list_3.index(i)] = pc_symbol
                break
    elif col_pol == 1 and str_pol == 1 and list_3[2] == "-":
        list_3[2] = user_choice
        check_win()
        for i in list_3:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_2[list_2.index(i)] = pc_symbol
                break
    elif col_pol == 1 and str_pol == 2 and list_4[2] == "-":
        list_4[2] = user_choice
        check_win()
        for i in list_4:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_4[list_4.index(i)] = pc_symbol
                break
    elif col_pol == 2 and str_pol == 0 and list_2[3] == "-":
        list_2[3] = user_choice
        check_win()
        for i in list_2:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_4[list_4.index(i)] = pc_symbol
                break
    elif col_pol == 2 and str_pol == 1 and list_3[3] == "-":
        list_3[3] = user_choice
        check_win()
        for i in list_3:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_2[list_2.index(i)] = pc_symbol
                break
    elif col_pol == 2 and str_pol == 2 and list_4[3] == "-":
        list_4[3] = user_choice
        check_win()
        for i in list_4:
            if i == "-":
                print("\n \n Мой ход)\n \n")
                list_3[list_3.index(i)] = pc_symbol
                break
    else:
        print(str.upper(("\n \n \nЛибо введены некорректные значения - либо выбрана занятая ячейка! \n"
                        "Посмотрите на игровое поле еще раз и введите корректные значения столбца и строки!\n \n")))
    print(f"{("    ").join(list_1)}\n{("    ").join(list_2)}\n{("    ").join(list_3)}\n{("    ").join(list_4)} \n")



