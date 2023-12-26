import random as ran # Импорт библиотеки для рандомизации

class GameException(Exception):
    "Класс исключений(размещение, некорректные выстрелы)"
    pass


class MissBoardException(GameException):
    "Выстрелы за границы поля"
    def __str__(self):
        return "Вы стреляете за границы игрового поля!"


class RepeatShotException(GameException):
    "Повторные выстрелы"
    def __str__(self):
        return "Сюда уже стреляли!!!"


class WrongPlacedShipException(GameException):
    "Невозможность размещения корабля"
    pass

class Points:
    "Класс координат со сравнением"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"





class Ship:
    "Класс кораблей с длинной и ориентациейс добавлением координат в список"
    def __init__(self, bow, len, orient):
        self.bow = bow
        self.len = len
        self.orient = orient
        self.lives = len

    @property
    def points(self):
        ship_points = []
        for i in range(self.len):
            current_x = self.bow.x
            current_y = self.bow.y

            if self.orient == 0:
                current_x += i

            elif self.orient == 1:
                current_y += i

            ship_points.append(Points(current_x, current_y))

        return ship_points

    def shoots(self, shot):
        return shot in self.points


class Board:
    "Класс игровой доски с методами размещения кораблей, отрисовки в консоли поля, выстрелов, попаданий. Проверка уничтожения корабля)"
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def add_ship(self, ship):

        for d in ship.points:
            if self.out(d) or d in self.busy:
                raise WrongPlacedShipException()
        for d in ship.points:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.points:
            for dx, dy in near:
                cur = Points(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def __str__(self):
        res = ""
        res += "   1  2  3  4  5  6 "
        for i, row in enumerate(self.field):
            res += f"\n{i + 1}  " + "  ".join(row) + " "

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise MissBoardException()

        if d in self.busy:
            raise RepeatShotException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.points:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship)
                    print("Потопил!!!")
                    return False
                else:
                    print("Попадание!")
                    return True

        self.field[d.x][d.y] = "."
        print("Мимо! 😝")
        return False

    def begin(self):
        self.busy = []


class Player:
    "Класс Игроков"
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except GameException as e:
                print(e)


class II(Player):
    "Дочерний от класса играков класс ИИ с методом создания рандомных координат для хода"
    def ask(self):
        d = Points(ran.randint(0, 5), ran.randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    "Дочерний от класса играков класс пользователя с методом для ввода координат выстрела"
    def ask(self):
        while True:
            cords = input("Стреляйте: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Points(x - 1, y - 1)


class Game:
    "Класс Игры с созданием игровых полей, рандомное размещение кораблей с исключением, с циклом ходов"
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ii = II(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Points(ran.randint(0, 6), ran.randint(0, 6)), l, ran.randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except WrongPlacedShipException:
                    pass
        board.begin()
        return board

    def welkom(self):
        "Класс Приветствие"
        print(" Добро пожаловать в игру! \n Для ввода координат выстрела \n введите сначала номер строки, \n "
              "а затем через пробел номер столбца и нажмите Enter!")


    def cicle(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска ИИ:")
            print(self.ii.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит ИИ!")
                repeat = self.ii.move()
            if repeat:
                num -= 1

            if self.ii.board.count == 7:
                print("-" * 20)
                print("УРА! Победа пользователя!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("ИИ Оказался Сильней!")
                break
            num += 1

    def start(self):
        self.welkom()
        self.cicle()


g = Game()
g.start()

