import sys #Импортирую модуль для использования exit()
import random as ran #

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

game_board = ["0",  "1",  "2", "0", "-", "-", "-", "1", "-", "-", "-", "2", "-", "-", "-"]
list_win_combo = [(4, 5, 6), (8, 9, 10), (12, 13, 14), (4, 8, 12), (5, 9, 13), (6, 10, 14), (4, 9, 14), (6, 9, 12)]

#Объяснения правил игроку
print(f"Тепеть о правилах!!! Игровое поле состоит из трёх столбцов и трёх строк. Они пронумерованы!  \n"
      f"{f"      {"     ".join(game_board[0: 3])}\n{"     ".join(game_board[3: 7])}\n{"     ".join(game_board[7: 11])}\n"
      f"{"     ".join(game_board[11: 15])}"} \n"
      "Сперва Вам предоставится выбор номера столбца, а затем номера строки. \n"
      "После осуществления выбора игровое поле обновится и, выбраный вами символ, \nпоявится на перекрестье" 
      " выбраных вами номеров столбца и строки. После - ход за мной)")

#
def bot_moves():
    print("\n \n Мой ход)\n \n")
    empty_indexes = [""]
    for i, element in enumerate(game_board):
        if element == "-":
            empty_indexes.append(i)
    if empty_indexes:
        bot_choice = ran.choice(empty_indexes)
        game_board[bot_choice] = pc_symbol


#Функция для проверки алгоритмов победы и завершения программы
def check_win():
    for ind_1, ind_2, ind_3 in list_win_combo:
        if "x" == game_board[ind_1] and "x" == game_board[ind_2] and "x" == game_board[ind_3]:
            print("\n \n УРА ИЛИ НЕ УРА, НО ПОБЕДИЛ  'Х' ! \n \n")
            print(
                f"      {"     ".join(game_board[0: 3])}\n{"     ".join(game_board[3: 7])}\n{"     ".join(game_board[7: 11])}\n"
                f"{"     ".join(game_board[11: 15])}")
            sys.exit()
        elif "0" == game_board[ind_1] and "0" == game_board[ind_2] and "0" == game_board[ind_3]:
            print("\n \n УРА ИЛИ НЕ УРА, НО ПОБЕДИЛ  '0' ! \n \n")
            print(
                f"      {"     ".join(game_board[0: 3])}\n{"     ".join(game_board[3: 7])}\n{"     ".join(game_board[7: 11])}\n"
                f"{"     ".join(game_board[11: 15])}")
            sys.exit()

#Игровой цикл с ходами игрока и компьютера с фильтром от недействительного ввода
while True:
    col_pol = int(input("Введите цифру с номером столбца: "))
    str_pol = int(input("Введите цифру с номером строки: "))
    if col_pol == 0 and str_pol == 0 and game_board[4] == "-":
        game_board[4] = user_choice
        check_win()
        bot_moves()
        check_win()
    elif col_pol == 0 and str_pol == 1 and game_board[8] == "-":
        game_board[8] = user_choice
        check_win()
        bot_moves()
        check_win()
    elif col_pol == 0 and str_pol == 2 and game_board[12] == "-":
        game_board[12] = user_choice
        check_win()
        bot_moves()
        check_win()
    elif col_pol == 1 and str_pol == 0 and game_board[5] == "-":
        game_board[5] = user_choice
        check_win()
        bot_moves()
        check_win()
    elif col_pol == 1 and str_pol == 1 and game_board[9] == "-":
        game_board[9] = user_choice
        check_win()
        bot_moves()
        check_win()
    elif col_pol == 1 and str_pol == 2 and game_board[13] == "-":
        game_board[13] = user_choice
        check_win()
        bot_moves()
        check_win()

    elif col_pol == 2 and str_pol == 0 and game_board[6] == "-":
        game_board[6] = user_choice
        check_win()
        bot_moves()
        check_win()
    elif col_pol == 2 and str_pol == 1 and game_board[10] == "-":
        game_board[10] = user_choice
        check_win()
        bot_moves()
        check_win()
    elif col_pol == 2 and str_pol == 2 and game_board[14] == "-":
        game_board[14] = user_choice
        check_win()
        bot_moves()
        check_win()
    else:
        print(str.upper(("\n \n \nЛибо введены некорректные значения - либо выбрана занятая ячейка! \n"
                        "Посмотрите на игровое поле еще раз и введите корректные значения столбца и строки!\n \n")))
    print(f"      {"     ".join(game_board[0: 3])}\n{"     ".join(game_board[3: 7])}\n{"     ".join(game_board[7: 11])}\n"
      f"{"     ".join(game_board[11: 15])}")

