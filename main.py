import curses
from pynput import keyboard
from curses.textpad import Textbox, rectangle
import random
from time import sleep

presslib = {}


# --- Собственная реализация is_pressed() ---
def press_evt(key):
    presslib[f"{key}".replace(".", "").replace("'", "").replace("Key", "")] = True


def release_evt(key):
    presslib[f"{key}".replace(".", "").replace("'", "").replace("Key", "")] = False


listener = keyboard.Listener(on_press=press_evt, on_release=release_evt)


def changeloc(text):
    layout = dict(zip(map(ord, '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''),
                      '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''))
    return text.translate(layout)


def is_pressed(key):
    if changeloc(key) in presslib:
        key = changeloc(key)
    try:
        if presslib[key] or presslib[changeloc(key)]:
            del presslib[key]
            return True
        else:
            return False
    except:
        return False


# --- --- --- --- --- --- --- --- --- --- ---


mkeff = {
    "3": [1.13, 1.29, 1.48, 1.71, 2.00, 2.35, 2.79, 3.35, 4.07, 5.00, 6.26, 7.96, 10.35, 13.80, 18.98, 27.11, 40.66,
          65.06, 113.85, 227.70, 569.25, 2277.00],
    "4": [1.18, 1.41, 1.71, 2.09, 2.58, 3.23, 4.09, 5.26, 6.88, 9.17, 12.51, 17.52, 25.30, 37.95, 59.64, 99.39, 178.91,
          357.81, 834.90, 2504.70, 12523.50],
    "5": [1.24, 1.56, 2.00, 2.58, 3.39, 4.52, 6.14, 8.50, 12.04, 17.52, 26.27, 40.87, 66.41, 113.85, 208.73, 417.45,
          939.26, 2504.70, 8766.45, 52598.70],
    "6": [1.30, 1.74, 2.35, 3.23, 4.52, 6.46, 9.44, 14.17, 21.89, 35.03, 58.38, 102.17, 189.75, 379.50, 834.90, 2087.25,
          6261.75, 25047.00, 175329.00],
    "7": [1.38, 1.94, 2.79, 4.09, 6.14, 9.44, 14.95, 24.47, 41.60, 73.95, 138.66, 277.33, 600.88, 1442.10, 3965.78,
          13219.25, 59486.63, 475893.00],
    "8": [1.46, 2.18, 3.35, 5.26, 8.50, 14.17, 24.47, 44.05, 83.20, 166.40, 356.56, 831.98, 2163.15, 6489.45, 23794.65,
          118973.25, 1070759.25],
    "9": [1.55, 2.48, 4.07, 6.88, 12.04, 21.89, 41.60, 83.20, 176.80, 404.10, 1010.26, 2828.73, 9193.39, 36773.55,
          202254.53, 2022545.25],
    "10": [1.65, 2.83, 5.00, 9.17, 17.52, 35.03, 73.95, 166.40, 404.10, 1077.61, 3232.84, 11314.94, 49031.40, 294188.40,
           3236072.40],
    "11": [1.77, 3.26, 6.26, 12.51, 26.27, 58.38, 138.66, 356.56, 1010.26, 3232.84, 12123.15, 56574.69, 367735.50,
           4412826.00],
    "12": [1.90, 3.81, 7.96, 17.52, 40.87, 102.17, 277.33, 831.98, 2828.73, 11314.94, 56574.69, 396022.85, 5148297.00],
    "13": [2.06, 4.50, 10.35, 25.30, 66.41, 189.75, 600.88, 2163.15, 9193.39, 49031.40, 367735.50, 5148297.00],
    "14": [2.25, 5.40, 13.80, 37.95, 113.85, 379.50, 1442.10, 6489.45, 36773.55, 294188.40, 4412826.00],
    "15": [2.48, 6.60, 18.98, 59.64, 208.73, 834.90, 3965.78, 23794.65, 202254.53, 3236072.40],
    "16": [2.75, 8.25, 27.11, 99.39, 417.45, 2087.25, 13219.25, 118973.25, 2022545.25],
    "17": [3.09, 10.61, 40.66, 178.91, 939.26, 6261.75, 59486.63, 1070759.25],
    "18": [3.54, 14.14, 65.06, 357.81, 2504.70, 25047.00, 475893.00],
    "19": [4.13, 19.80, 113.85, 834.90, 8766.45, 175329.00],
    "20": [4.95, 29.70, 227.70, 2504.70, 52598.70],
    "21": [6.19, 49.50, 569.25, 12523.50],
    "22": [8.25, 99.00, 2277.00],
    "23": [12.38, 297.00],
    "24": [25],
}
kenokeff = {
    "0": {
        "1": [0.7, 1.78], "2": [0, 2, 3.49], "3": [0, 1.1, 1.4, 24.2], "4": [0, 0, 2.2, 7.4, 90],
        "5": [0, 0, 1.5, 4.1, 12, 300], "6": [0, 0, 1.1, 2, 5.35, 100, 700], "7": [0, 0, 1.1, 1.6, 3.4, 14, 200, 700],
        "8": [0, 0, 1.1, 1.5, 1.95, 5.3, 28, 100, 800], "9": [0, 0, 1.1, 1.3, 1.45, 2.45, 10, 50, 300, 1000],
        "10": [0, 0, 1.1, 1.2, 1.3, 1.5, 3, 12, 55, 300, 1000]
    },
    "1": {
        "1": [0.4, 2.68], "2": [0, 1.7, 5.48], "3": [0, 0, 2.66, 49.95], "4": [0, 0, 1.6, 10.1, 100],
        "5": [0, 0, 1.4, 3.85, 13.2, 390], "6": [0, 0, 0, 3, 8.65, 175, 710], "7": [0, 0, 0, 2, 6.8, 30, 370, 800],
        "8": [0, 0, 0, 2, 3.94, 10.5, 60, 400, 900], "9": [0, 0, 0, 2, 2.4, 4.73, 14.5, 100, 500, 1000],
        "10": [0, 0, 0, 1.5, 2, 3.8, 8.5, 35, 200, 1000, 5000]
    },
    "2": {
        "1": [0, 3.88], "2": [0, 0, 16.82], "3": [0, 0, 0, 79.9], "4": [0, 0, 1.6, 10.1, 100],
        "5": [0, 0, 1.4, 3.85, 13.2, 390], "6": [0, 0, 0, 3, 8.65, 175, 710], "7": [0, 0, 0, 2, 6.8, 30, 370, 800],
        "8": [0, 0, 0, 2, 3.94, 10.5, 60, 400, 900], "9": [0, 0, 0, 2, 2.4, 4.73, 14.5, 100, 500, 1000],
        "10": [0, 0, 0, 1.5, 2, 3.8, 8.5, 35, 200, 1000, 5000]
    }
}
cookieskeff = [
    [0.1, 0.5, 1.7, 2.1, 2.8, 3.75, 20],
    [0, 0.1, 1.95, 2.95, 4, 5.2, 50],
    [0, 0, 1.3, 3.5, 5.9, 8, 100]
]

lad = [[0, 20], [0, 19], [1, 19], [3, 17], [0, 19], [2, 15], [3, 17], [7, 13], [8, 12], [0, 19], [0, 10], [0, 9],
       [0, 8]]

ladkeff = [[1, 1.06, 1.12, 1.19, 1.27, 1.36, 1.46, 1.58, 1.73, 1.9, 2.11, 2.38, 2.71],
           [1.06, 1.18, 1.33, 1.5, 1.72, 1.98, 2.31, 2.73, 3.28, 4.01, 5.01, 6.45, 8.6],
           [1.12, 1.33, 1.59, 1.93, 2.38, 2.98, 3.79, 4.92, 6.56, 9.03, 12.89, 19.34, 30.94],
           [1.19, 1.5, 1.93, 2.53, 3.37, 4.6, 6.44, 9.3, 13.95, 21.92, 36.53, 65.75, 131.51],
           [1.27, 1.72, 2.38, 3.37, 4.9, 7.36, 11.44, 18.6, 31.88, 58.45, 116.9, 263.01, 701.37],
           [1.36, 1.98, 2.98, 4.6, 7.36, 12.26, 21.46, 39.85, 79.7, 175.34, 438.36, 1320, 5260],
           [1.46, 2.31, 3.79, 6.44, 11.44, 21.46, 42.92, 92.98, 223.16, 613.7, 2050, 9210, 73640]]


def miner_reveal(screen, matrix, opened):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                col = 5
            elif not (matrix[i][j]) and opened[i][j]:
                col = 4
            elif not (matrix[i][j]) and not (opened[i][j]):
                col = 11
            screen.addstr(i * 2 + 2, j * 4 + 4, "  ", curses.color_pair(col))


def bet_blink(screen, bet):
    screen.addstr(3, 50, f" " * 50)
    screen.addstr(3, 50, f"Ставка: {bet:.2f}", curses.A_BLINK)
    screen.refresh()
    sleep(0.2)


def bal_error(screen, bal):
    screen.addstr(2, 50, f"Баланс: {bal:.2f}", curses.color_pair(1) | curses.A_BOLD)
    screen.refresh()
    sleep(0.3)


def cookies_state(arr):
    count = {i: arr.count(i) for i in arr}
    cl = sorted(list(count.values()))[::-1]
    if cl == [1, 1, 1, 1, 1]:
        return 0
    elif cl == [2, 1, 1, 1]:
        return 1
    elif cl == [2, 2, 1]:
        return 2
    elif cl == [3, 1, 1]:
        return 3
    elif cl == [3, 2]:
        return 4
    elif cl == [4, 1]:
        return 5
    elif cl == [5]:
        return 6


def keffcol(n, sel: bool = False):
    if not (sel):
        if 0 <= n < 1:
            return curses.color_pair(21)
        elif 1 <= n < 2:
            return curses.color_pair(16)
        elif 2 <= n < 5:
            return curses.color_pair(19)
        elif 5 <= n < 20:
            return curses.color_pair(13)
        elif 20 <= n:
            return curses.color_pair(18)
    else:
        if 0 <= n < 1:
            return curses.color_pair(30)
        elif 1 <= n < 2:
            return curses.color_pair(31)
        elif 2 <= n < 5:
            return curses.color_pair(32)
        elif 5 <= n < 20:
            return curses.color_pair(33)
        elif 20 <= n:
            return curses.color_pair(34)


def main(screen):
    # ------- НАСТРОЙКА ------- #
    listener.start()  # Запуск прослушивателя клавиш
    screen.nodelay(True)  # Отключаем ожидание ввода клавиш
    curses.use_default_colors()  # Используем стандартные цвета
    curses.curs_set(0)  # Отключаем курсор
    # ------- ПЕРЕМЕННЫЕ ------- #
    scene = 0  # Сцена
    game = 0  # Выбранная игра
    bal = 100.00  # Баланс
    bet = 10.0  # Ставка
    bombs = 4  # Количество бомб
    games = 7  # Количество режимов
    color = 1  # Выбранный цвет в рулетке
    wkeff = 2  # Коэфициент в рулетке
    size = 5  # Размер сетки в минёре
    kpx, kpy = 0, 0  # Положение игрока в кено
    risk = 0  # Риск в кено и кукисах
    fails = 3  # Провалы в лесенках
    ladpad = 9
    orel = True
    ksel = []
    line = {"char": "─", "size": 25 * 3}  # Линии снизу и сверху
    coinsize = 10
    cookies = [
        {"color": curses.color_pair(13), "char": "✚", "index": 0},
        {"color": curses.color_pair(14), "char": "☂", "index": 1},
        {"color": curses.color_pair(18), "char": "✦", "index": 2},
        {"color": curses.color_pair(20), "char": "✱", "index": 3},
        {"color": curses.color_pair(21), "char": "❤", "index": 4},
        {"color": curses.color_pair(19), "char": "■", "index": 5},
        {"color": curses.color_pair(15), "char": "☁", "index": 6}
    ]
    nowait = False
    # ------- ЦВЕТА ------- #
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Красный цвет
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Голубой цвет
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Синий фон + белый текст
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)  # Белый фон + красный текст
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_RED)  # Красное всё
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_CYAN)  # Красный текст + голубой фон
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Зелёный цвет
    curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_GREEN)  # Зелёное всё
    curses.init_color(101, 550, 550, 550)
    curses.init_pair(9, 101, -1)  # Серый текст
    curses.init_color(102, 10, 10, 300)
    curses.init_color(103, 400, 200, 600)
    curses.init_pair(10, 103, 102)  # Серый текст
    curses.init_color(104, 200, 200, 400)
    curses.init_color(106, 400, 400, 700)
    curses.init_pair(11, 106, 104)
    curses.init_color(105, 933, 509, 933)
    curses.init_pair(12, 105, -1)
    curses.init_color(107, 100, 700, 100)
    curses.init_color(108, 20, 130, 20)
    curses.init_pair(13, 107, 108)  # Fancy Зелёный 13
    curses.init_color(109, 750, 200, 1000)
    curses.init_color(110, 125, 75, 250)
    curses.init_pair(14, 109, 110)  # Fancy Фиолетовый 14
    curses.init_color(111, 800, 500, 1000)
    curses.init_color(112, 340, 150, 650)
    curses.init_pair(15, 111, 112)  # Fancy Голубой 15
    curses.init_color(113, 820, 820, 820)
    curses.init_color(114, 150, 150, 150)
    curses.init_color(99, 400, 400, 400)
    curses.init_pair(16, 113, 114)  # Fancy Gray 16
    curses.init_pair(99, 99, -1)  # Gray Text 17
    curses.init_color(115, 1000, 760, 0)
    curses.init_color(116, 230, 80, 0)
    curses.init_pair(18, 115, 116)  # Fancy Yellow 18
    curses.init_color(117, 0, 760, 910)
    curses.init_color(118, 0, 120, 160)
    curses.init_pair(19, 117, 118)  # Fancy Cyan 19
    curses.init_color(119, 1000, 450, 0)
    curses.init_color(120, 230, 50, 0)
    curses.init_pair(20, 119, 120)  # Fancy Orange 20
    curses.init_color(121, 900, 50, 50)
    curses.init_color(122, 250, 10, 10)
    curses.init_pair(21, 121, 122)  # Fancy Red 21
    curses.init_color(130, 560, 5, 5)
    curses.init_pair(30, curses.COLOR_WHITE, 130)  # Sel Red 30
    curses.init_color(131, 300, 300, 300)
    curses.init_pair(31, curses.COLOR_WHITE, 131)  # Sel Gray 31
    curses.init_color(132, 35, 230, 410)
    curses.init_pair(32, curses.COLOR_WHITE, 132)  # Sel Blue 32
    curses.init_color(133, 0, 410, 50)
    curses.init_pair(33, curses.COLOR_WHITE, 133)  # Sel Green 33
    curses.init_color(134, 480, 370, 0)
    curses.init_pair(34, curses.COLOR_WHITE, 134)  # Sel Yellow 34

    while True:
        screen.getch()
        screen.refresh()
        if nowait:
            nowait = False
        else:
            sleep(0.01)
        if is_pressed("esc"):
            break
        if is_pressed("b"):
            screen.getch()
            curses.curs_set(1)
            inputwin = curses.newwin(1, 10, 3, 58)
            box = Textbox(inputwin)
            screen.refresh()
            box.edit()
            try:
                bet = float(box.gather())
            except:
                curses.curs_set(0)
                screen.clear()
                continue
            bet = round(bet, 2)
            screen.clear()
            curses.curs_set(0)
        if is_pressed("a"):
            bet = bal
            bet_blink(screen, bet)
        if is_pressed("w"):
            bet *= 2
            bet = round(bet, 2)
            bet_blink(screen, bet)
        if is_pressed("s"):
            bet *= 0.5
            bet = round(bet, 2)
            bet_blink(screen, bet)

        if scene == 0:
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(8, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(2, 4, "XCasino", curses.A_BOLD | curses.color_pair(12))
            screen.addstr(2, 12, "- Симулятор казино")
            screen.addstr(6, 4, "Нажмте Пробел, чтобы начать")
            screen.addstr(2, 50, f"Баланс: {bal:.2f}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}{' ' * 10}")
            dec = [curses.A_NORMAL] * games
            dec[game] = curses.color_pair(2) | curses.A_BOLD
            screen.addstr(4, 4, "Crash", dec[0])
            screen.addstr(4, 11, "Miner", dec[1])
            screen.addstr(4, 18, "Wheel", dec[2])
            screen.addstr(4, 25, "Keno", dec[3])
            screen.addstr(4, 31, "Coin", dec[4])
            screen.addstr(4, 37, "Cookies", dec[5])
            screen.addstr(4, 46, "Ladders", dec[6])
            if is_pressed("right"):
                game += 1
                game %= games
            if is_pressed("left"):
                game -= 1
                game %= games
            if is_pressed("space"):
                for _ in range(3):
                    screen.addstr(6, 4, "Нажмте Пробел, чтобы начать", curses.color_pair(2) | curses.A_BOLD)
                    screen.refresh()
                    sleep(0.1)
                    screen.addstr(6, 4, "Нажмте Пробел, чтобы начать", curses.color_pair(2))
                    screen.refresh()
                    sleep(0.1)
                scene = game + 1
                screen.clear()

        elif scene == 1:
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(8, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(2, 50, f"Баланс: {bal:.2f}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}")
            screen.addstr(4, 50, f"B - изменить ставку", curses.color_pair(9))
            screen.addstr(5, 50, f"Пробел - начать игру", curses.color_pair(9))
            screen.addstr(6, 50, f"Q - вернуться в меню", curses.color_pair(9))
            screen.addstr(4, 4, f"{0:.2f}  ", curses.A_BOLD)

            if is_pressed("q"):
                scene = 0
                screen.clear()
            if is_pressed("space"):
                if bal < bet:
                    bal_error(screen, bal)
                    continue
                screen.addstr(4, 50, " " * 25)
                screen.addstr(5, 50, f"Пробел - остановить      ", curses.color_pair(9))
                screen.addstr(6, 50, " " * 25)
                bal -= bet
                bal = round(bal, 2)
                crash = round((random.randint(0, 3000) / 100), 2)
                kof = 0
                koff = 0
                while kof <= crash:
                    kof += 0.01
                    kof = round(kof, 2)
                    if kof > random.randint(0, 1000):
                        break
                    screen.addstr(4, 4, f"{kof:.2f}", keffcol(kof))
                    if koff != 0:
                        screen.addstr(4, 10, f"{koff:.2f}", keffcol(koff, True))
                    if is_pressed("space") and koff == 0:
                        koff = kof
                        screen.addstr(5, 50, " " * 25)
                    screen.refresh()
                    if kof <= 1:
                        sleep(0.01)
                    else:
                        sleep(1 / (kof * (10 if (koff == 0) else 50)))
                screen.addstr(4, 4, f"{kof:.2f}  ", curses.color_pair(1) | curses.A_BOLD)
                bal += bet * koff
                bal = round(bal, 2)
                screen.addstr(2, 50, f"Баланс: {bal:.2f}", curses.color_pair(2))
                screen.refresh()
                sleep(2.5)
                screen.clear()

        elif scene == 2:
            screen.addstr(9, 50, f"Пробел - начать игру", curses.color_pair(9))
            screen.addstr(10, 50, f"Q - вернуться в меню", curses.color_pair(9))
            screen.addstr(4, 50, f"B - изменить ставку", curses.color_pair(9))
            screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}{' ' * 10}")
            screen.addstr(6, 50, f"Мин: {bombs}")
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(12, 0, line['char'] * line['size'], curses.color_pair(10))
            for i in range(5):
                for j in range(5):
                    screen.addstr(i * 2 + 2, j * 4 + 4, "  ", curses.color_pair(11))
            if is_pressed("up") and (3 <= bombs < 24):
                bombs += 1
            if is_pressed("down") and (3 < bombs <= 24):
                bombs -= 1
            if is_pressed("q"):
                scene = 0
                screen.clear()
            if is_pressed("space"):
                if bal < bet:
                    bal_error(screen, bal)
                    continue
                screen.addstr(9, 50, f"R - случайная ячейка", curses.color_pair(9))
                screen.addstr(10, 50, f"Q - забрать выигрыш ", curses.color_pair(9))
                screen.addstr(4, 50, " " * 20)
                matrix = [[0 for _ in range(size)] for _ in range(size)]
                inds = [i for i in range(size ** 2)]
                for _ in range(bombs):
                    elem = random.choice(inds)
                    inds.remove(elem)
                    matrix[elem % size][elem // size] = 1
                opened = [[0 for _ in range(size)] for _ in range(size)]
                keff = 1
                bal -= bet
                bal = round(bal, 2)
                px, py = 0, 0
                sleep(0.1)
                while True:
                    screen.addstr(5, 50, f"Множитель: {keff:.2f}x ")
                    if is_pressed("up"): py -= 1
                    if is_pressed("down"): py += 1
                    if is_pressed("right"): px += 1
                    if is_pressed("left"): px -= 1
                    if is_pressed("r"): px, py = random.randrange(size), random.randrange(size)
                    if is_pressed("q"):
                        miner_reveal(screen, matrix, opened)
                        screen.addstr(5, 25, f"Вы забрали {round(keff * bet, 2)}", curses.color_pair(7) | curses.A_BOLD)
                        bal += bet * keff
                        bal = round(bal, 2)
                        break
                    if is_pressed("space"):
                        if matrix[py][px]:
                            miner_reveal(screen, matrix, opened)
                            screen.addstr(5, 25, "Вы проиграли!", curses.color_pair(1) | curses.A_BOLD)
                            break
                        opened[py][px] = 1
                        keff = mkeff[str(bombs)][sum([sum(i) for i in opened]) - 1]
                        if sum([sum(i) for i in opened]) == (size ** 2) - bombs:
                            miner_reveal(screen, matrix, opened)
                            screen.addstr(5, 25, "Вы победили!", curses.color_pair(7) | curses.A_BOLD)
                            bal += bet * keff
                            bal = round(bal, 2)
                            break
                    px %= size;
                    py %= size
                    for i in range(len(matrix)):
                        for j in range(len(matrix[i])):
                            col = 4 if opened[i][j] else 11
                            screen.addstr(i * 2 + 2, j * 4 + 4, f"  ", curses.color_pair(col))
                            screen.addstr(i * 2 + 2, j * 4 + 3, "▶" if (i == py and j == px) else " ")
                            screen.addstr(i * 2 + 2, j * 4 + 6, "◀" if (i == py and j == px) else " ")
                    screen.refresh()
                    sleep(0.01)
                screen.addstr(2, 50, f"Баланс: {bal:.2f}         ", curses.color_pair(2))
                screen.refresh()
                sleep(2.5)
                screen.clear()

        elif scene == 3:  # Колесо
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(8, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(4, 50, f"B - изменить ставку", curses.color_pair(9))
            screen.addstr(5, 50, f"Пробел - крутить колесо", curses.color_pair(9))
            screen.addstr(6, 50, f"Q - вернуться в меню", curses.color_pair(9))
            screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}{' ' * 10}")
            screen.addstr(2, 24, f"{wkeff}		  ")
            wheel = [0, 1, 0, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1]
            screen.addstr(4, 24, f"▼")
            if color == 2:
                dec, wkeff = curses.color_pair(8), 14
            elif color == 1:
                dec, wkeff = curses.color_pair(5), 2
            elif color == 0:
                dec, wkeff = curses.color_pair(3), 2
            screen.addstr(3, 23, f"   ", dec)
            screen.addstr(3, 21, f"◀")
            screen.addstr(3, 27, f"▶")
            i = 0
            for num in wheel:
                if num == 2:
                    dec = curses.color_pair(8)
                elif num == 1:
                    dec = curses.color_pair(5)
                elif num == 0:
                    dec = curses.color_pair(3)
                screen.addstr(5, i * 3 + 2, f"   ", dec)
                i += 1
            if is_pressed("right"):
                color += 1
                color %= 3
            elif is_pressed("left"):
                color -= 1
                color %= 3
            elif is_pressed("q"):
                scene = 0
                screen.clear()
            elif is_pressed("space"):
                screen.addstr(4, 50, " " * 25)
                screen.addstr(5, 50, " " * 25)
                screen.addstr(6, 50, " " * 25)
                if bal < bet:
                    bal_error(screen, bal)
                    continue
                bal = bal - bet
                bal = round(bal, 2)
                screen.addstr(2, 50, f"Баланс: {bal:.2f}" + (" " * 20), curses.color_pair(2))
                for ix in range(0, random.randint(25, 50)):
                    i = 0
                    tmp = wheel[0]
                    wheel = wheel[1:len(wheel)]
                    wheel.append(tmp)
                    for num in wheel:
                        if num == 2:
                            dec = curses.color_pair(8)
                        elif num == 1:
                            dec = curses.color_pair(5)
                        elif num == 0:
                            dec = curses.color_pair(3)
                        screen.addstr(5, i * 3 + 2, f"   ", dec)
                        i += 1
                    screen.refresh()
                    sleep((1 - ((100 - ix) / 100)))
                sleep(1)
                if wheel[7] == 2:
                    dec = curses.color_pair(8)
                elif wheel[7] == 1:
                    dec = curses.color_pair(5)
                elif wheel[7] == 0:
                    dec = curses.color_pair(3)
                screen.addstr(5, 2, f"   " * 15, dec)
                screen.refresh()
                if color == wheel[7]:
                    bal += wkeff * bet
                sleep(1.5)

        elif scene == 4:  # Кено
            screen.addstr(9, 50, f"Enter - начать игру", curses.color_pair(9))
            screen.addstr(10, 50, f"Q - вернуться в меню", curses.color_pair(9))
            screen.addstr(4, 50, f"B - изменить ставку", curses.color_pair(9))
            screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}{' ' * 10}")
            dec = [curses.A_NORMAL] * 3
            dec[risk] = curses.color_pair(14) | curses.A_BOLD
            screen.addstr(12, 4, "Риск:")
            screen.addstr(12, 12, "1: Низкий", dec[0])
            screen.addstr(12, 25, "2: Средний", dec[1])
            screen.addstr(12, 39, "3: Высокий", dec[2])
            screen.addstr(5, 50, " " * 30)
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(14, 0, line['char'] * line['size'], curses.color_pair(10))
            for i in range(5):
                for j in range(8):
                    col = 15 if (i * 8 + j in ksel) else 11
                    screen.addstr(i * 2 + 2, j * 4 + 3, "▶" if (i == kpy and j == kpx) else " ")
                    screen.addstr(i * 2 + 2, j * 4 + 6, "◀" if (i == kpy and j == kpx) else " ")
                    screen.addstr(i * 2 + 2, j * 4 + 4, f"{i * 8 + j + 1:02}", curses.color_pair(col))
            if is_pressed("1"): risk = 0
            if is_pressed("2"): risk = 1
            if is_pressed("3"): risk = 2
            if is_pressed("up"):
                kpy -= 1
                kpy %= 5
            if is_pressed("down"):
                kpy += 1
                kpy %= 5
            if is_pressed("right"):
                kpx += 1
                kpx %= 8
            if is_pressed("left"):
                kpx -= 1
                kpx %= 8
            elif is_pressed("q"):
                scene = 0
                screen.clear()
            if is_pressed("enter"):
                if len(ksel) == 0:
                    continue
                if bal < bet:
                    bal_error(screen, bal)
                    continue
                bal -= bet
                screen.addstr(4, 50, " " * 20)
                screen.addstr(9, 50, " " * 20)
                screen.addstr(10, 50, " " * 20)
                screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
                matrix = [i for i in range(40)]
                vipalo = []
                win = 0
                for _ in range(10):
                    num = random.choice(matrix)
                    matrix.remove(num)
                    vipalo.append(num)
                for i in range(5):
                    for j in range(8):
                        itr = i * 8 + j
                        if (itr in ksel) and (itr in vipalo):
                            col, win = 13, win + 1
                        elif (itr in ksel) and not (itr in vipalo):
                            col = 15
                        elif not (itr in ksel) and (itr in vipalo):
                            col = 32
                        elif not (itr in ksel) and not (itr in vipalo):
                            col = 11
                        screen.addstr(i * 2 + 2, j * 4 + 4, f"{i * 8 + j + 1:02}", curses.color_pair(col))
                keff = kenokeff[str(risk)][str(len(ksel))][win]
                screen.addstr(5, 50, f"Множитель: {keff}")
                bal += bet * keff
                bal = round(bal, 2)
                screen.refresh()
                sleep(1)
            # screen.clear()
            if is_pressed("space"):
                tmp = kpy * 8 + kpx
                if tmp in ksel:
                    ksel.remove(tmp)
                else:
                    if len(ksel) >= 10:
                        continue
                    ksel.append(tmp)

        elif scene == 5:  # Монетка
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(8, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(6, 4, f"Пробел - начать игру" + " " * 10)
            screen.addstr(6, 50, f"Q - вернуться в меню", curses.color_pair(9))
            screen.addstr(4, 50, f"B - изменить ставку", curses.color_pair(9))
            screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}{' ' * 10}")
            for j in range(coinsize):
                screen.addstr(3, 4 + (j * 4), " ○ ", curses.color_pair(16))
            if is_pressed("q"):
                scene = 0
                screen.clear()
            if is_pressed("space"):
                if bal < bet:
                    bal_error(screen, bal)
                    continue
                bal -= bet
                screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
                keff = 1
                screen.addstr(5, 50, "Пробел - бросить монетку" + " " * 10, curses.color_pair(9))
                screen.addstr(6, 50, "Q - забрать выигрыш" + " " * 10, curses.color_pair(9))
                screen.refresh()
                orelnow = [bool(random.randint(0, 1)) for _ in range(coinsize)]
                i = 0
                while i != coinsize:
                    if is_pressed("space"):
                        for j in range(coinsize):
                            screen.addstr(3, 4 + (j * 4), " ● " if i >= j else " ○ ", (
                                curses.color_pair(13) if orelnow[j] else curses.color_pair(
                                    14)) if i >= j else curses.color_pair(16))
                        if orelnow[i] == orel:
                            keff *= 2
                        else:
                            keff = 0
                            break
                        i += 1
                    if is_pressed("q"):
                        break
                    if is_pressed("right"): orel = False
                    if is_pressed("left"): orel = True
                    screen.addstr(6, 4, "Сторона:" + " " * 15)
                    screen.addstr(6, 14, "Орёл", curses.color_pair(13) if orel else curses.A_NORMAL)
                    screen.addstr(6, 20, "Решка", curses.color_pair(14) if not (orel) else curses.A_NORMAL)
                    screen.addstr(4, 50, f"Множитель: {keff}x" + " " * 10)
                    screen.refresh()
                    sleep(0.01)
                screen.addstr(4, 50, f"Множитель: {keff}x" + " " * 10)
                screen.addstr(6, 4, "Нажмите на Пробел, чтобы продолжить" + " " * 10)
                screen.addstr(3, 4, "  " * 20)
                for j in range(len(orelnow)):
                    screen.addstr(3, 4 + (j * 4), " ● " if i > j else " ○ ",
                                  curses.color_pair(13) if orelnow[j] else curses.color_pair(14))
                bal += bet * keff
                bal = round(bal, 2)
                screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
                screen.refresh()
                while not (is_pressed("space")): sleep(0.01)
                screen.clear()

        elif scene == 6:  # Печеньки
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(10, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(6, 4, f"Пробел - начать игру" + " " * 10)
            screen.addstr(6, 50, f"Q - вернуться в меню", curses.color_pair(9))
            screen.addstr(4, 50, f"B - изменить ставку", curses.color_pair(9))
            screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}{' ' * 10}")
            dec = [curses.A_NORMAL] * 3
            dec[risk] = curses.color_pair(14) | curses.A_BOLD
            screen.addstr(8, 4, "Риск:")
            screen.addstr(8, 12, "1: Низкий", dec[0])
            screen.addstr(8, 25, "2: Средний", dec[1])
            screen.addstr(8, 39, "3: Высокий", dec[2])
            for j in range(5):
                screen.addstr(4, 4 + (j * 9), "▂▃▄▄▄▃▂", curses.color_pair(17))
            if is_pressed("1"): risk = 0
            if is_pressed("2"): risk = 1
            if is_pressed("3"): risk = 2
            if is_pressed("q"):
                scene = 0
                screen.clear()
            if is_pressed("space"):
                if bal < bet:
                    bal_error(screen, bal)
                    continue
                bal -= bet
                screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
                keff = 1
                screen.addstr(6, 50, " " * 25, curses.color_pair(9))
                screen.addstr(4, 50, " " * 25, curses.color_pair(9))
                state = 0
                items = [random.choice(cookies) for _ in range(5)]

                for j in range(5):
                    item = items[j]
                    screen.addstr(2, 6 + (j * 9), f"   ", item['color'])
                    screen.addstr(3, 6 + (j * 9), f" {item['char']} ", item['color'])
                    if (items[j] in items[:j]):
                        for jj in range(len(items[:j + 1])):
                            if items[jj] == items[j]:
                                screen.addstr(4, 4 + (jj * 9), "▂▃▄▄▄▃▂", curses.color_pair(2))
                    screen.refresh()
                    sleep(0.3)
                screen.addstr(6, 4, "Нажмите на Пробел, чтобы продолжить" + " " * 10)
                keff = cookieskeff[risk][cookies_state([_["index"] for _ in items])]
                screen.addstr(5, 50, f"Множитель: {keff}")
                bal += bet * keff
                bal = round(bal, 2)
                screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
                screen.refresh()
                while not (is_pressed("space")): sleep(0.01)
                screen.clear()

        elif scene == 7:  # Лесенки
            screen.addstr(0, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(29, 0, line['char'] * line['size'], curses.color_pair(10))
            screen.addstr(6, 50, "Q - вернуться в меню", curses.color_pair(9))
            screen.addstr(5, 50, f"Опасных зон: {fails}")
            screen.addstr(4, 50, "B - изменить ставку", curses.color_pair(9))
            screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
            screen.addstr(3, 50, f"Ставка: {bet:.2f}{' ' * 10}")
            for i in range(len(lad)):
                screen.addstr(26 - i * 2, 1, " " * 7)
                screen.addstr(26 - i * 2, 1, f"{ladkeff[fails - 1][i]}x", keffcol(ladkeff[fails - 1][i]))
                for j in range(lad[i][1]):
                    screen.addstr(26 - (i * 2), ladpad + (lad[i][0] * 3) + j * 3, "▁▁▁",
                                  curses.color_pair(17) if (j + lad[i][0]) % 2 == 0 else curses.color_pair(9))
            if is_pressed("up") and fails + 1 <= 7: fails += 1
            if is_pressed("down") and fails - 1 >= 1: fails -= 1
            if is_pressed("q"):
                scene = 0
                screen.clear()
            if is_pressed("space"):
                if bal < bet:
                    bal_error(screen, bal)
                    continue
                bal -= bet
                screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
                screen.addstr(6, 50, f" " * 25)
                screen.addstr(4, 50, f" " * 25)
                px = 0
                py = -1
                keff = 1
                allfails = [random.sample(range(lad[i][0], lad[i][0] + lad[i][1]), fails) for i in range(len(lad))]
                while True:
                    for i in range(-1, len(lad)):
                        if i == -1:
                            for j in range(20):
                                screen.addstr(26 - (i * 2), ladpad + j * 3, "▆▇▆" if px == j and py == i else "   ",
                                              curses.A_NORMAL)
                        else:
                            for j in range(lad[i][1]):
                                #: dec = curses.color_pair(15)
                                if j + lad[i][0] in allfails[i] and py >= i:
                                    dec = curses.color_pair(21)
                                elif (j + lad[i][0]) % 2 == 0:
                                    dec = curses.color_pair(17)
                                else:
                                    dec = curses.color_pair(9)
                                screen.addstr(26 - (i * 2), ladpad + (lad[i][0] * 3) + j * 3,
                                              "▆▇▆" if px == j and py == i else "▁▁▁", dec)
                    if is_pressed("right") and px + 1 < (lad[py][1] if py >= 0 else 20): px += 1
                    if is_pressed("left") and px - 1 >= 0: px -= 1
                    if is_pressed("space") and lad[py + 1][0] <= px + lad[py][0] < lad[py + 1][0] + lad[py + 1][1]:
                        px -= lad[py + 1][0] - lad[py][0]
                        py += 1
                        if px + lad[py][0] in allfails[py]:
                            keff = 0
                            break
                        keff = ladkeff[fails - 1][py]
                        if py >= 12:
                            break
                    if is_pressed("q"):
                        break
                    sleep(0.01)
                    screen.refresh()
                for i in range(len(lad)):
                    for j in range(lad[i][1]):
                        if j + lad[i][0] in allfails[i]:
                            dec = curses.color_pair(21)
                        elif (j + lad[i][0]) % 2 == 0:
                            dec = curses.color_pair(17)
                        else:
                            dec = curses.color_pair(9)
                        screen.addstr(26 - (i * 2), ladpad + (lad[i][0] * 3) + j * 3,
                                      "▆▇▆" if px == j and py == i else "▁▁▁", dec)
                screen.addstr(28, 4, "   " * 20)
                bal += bet * keff
                bal = round(bal, 2)
                screen.addstr(2, 50, f"Баланс: {bal:.2f}{' ' * 10}", curses.color_pair(2))
                screen.addstr(10, 11, f"Пробел - продолжить", curses.color_pair(9))
                screen.refresh()
                while not (is_pressed("space")): sleep(0.01)
                screen.clear();
                nowait = True


curses.wrapper(main)
