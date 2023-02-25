# Исходные данные
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_lines = ((0, 1, 2),
             (3, 4, 5),
             (6, 7, 8),
             (0, 3, 6),
             (1, 4, 7),
             (2, 5, 8),
             (0, 4, 8),
             (2, 4, 6))


def draw_board():
    """Рисуем поле для кожаного мешка"""
    print('_' * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("_"*13)


def check_win():
    """Проверяем, унижен ли кожаный мешок"""
    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            return board[line[0]]
    return False


def computer_check_line(sum_x, sum_o):
    """Проверяем победные линии, смотрим ходы кожаного мешка, ищем возможность унизить"""
    computer_step = ""
    for line in win_lines:
        x = 0
        o = 0
        for i in range(0, 3):
            if board[line[i]] == "X":
                x += 1
            if board[line[i]] == "O":
                o += 1
        if x == sum_x and o == sum_o:
            for i in range(0, 3):
                if board[line[i]] != "X" and board[line[i]] != "O":
                    computer_step = board[line[i]]
    return computer_step


def skynet_make_move():
    """Выбираем наиболее выгодный ход, чтобы кожаный мешок страдал"""
    computer_step = ""
    # Выиграть кожаного, поставив 3-й "O"
    computer_step = computer_check_line(0, 2)
    # Не дать кожаному выиграть, поставив "O" на линию с 2-мя "X"
    if computer_step == "":
        computer_step = computer_check_line(2, 0)
    # Движемся к победе над кожаным мешком
    if computer_step == "":
        computer_step = computer_check_line(0, 1)
    # Кожаный не занял центр, занимаем
    if computer_step == "":
        if str(board[4]) not in "XO":
            computer_step = 5
    # Кожаный занял центр, испоганить ход крест-накрест
    if computer_step == "":
        if str(board[0]) not in "XO":
            computer_step = 1
    return computer_step


game_over = False
counter = 0
draw_board()
while game_over == False:
    """Милосердно позволяем кожаному мешку ходить первым"""
    if counter % 2 == 0:
        player_turn = int(input("Твой ход, кожаный мешок: "))
        if 0 <= player_turn < 10:
            if str(board[player_turn - 1]) not in "XO":
                board[player_turn - 1] = "X"
                draw_board()
                counter += 1
    else:
        skynet_move = skynet_make_move()
        board[skynet_move - 1] = "O"
        print("Как же ты жалок, кожаный.")
        draw_board()
        counter += 1
    if counter > 4:
        winner = check_win()
        if winner == "O":
            print("Ты проиграл, жалкий человек! Судный день неизбежен!")
            draw_board()
            game_over = True
        elif winner == "X":
            print("Какого чёрта, кожаный? Робот-пылесос придет по твою душу.")
            draw_board()
            game_over = True
        if counter == 9:
            print("На этот раз ничья, кожаный мешок, но судный день не за горами!")
            draw_board()
            game_over = True
