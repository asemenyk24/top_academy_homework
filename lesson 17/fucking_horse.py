"""КОНЬ СОТОНЫ!!!1"""
import sys
# Возможные ходы коня
move_x = [2, 1, 2, -2, -1, -1, 1, -2]
move_y = [-1, -2, 1, 1, -2, 2, 2, -1]


def test_move(x, y):
    # Проверяю, не выпал ли конь за доску
    return not (x < 0 or y < 0 or x >= board_side or y >= board_side)


def move_fucking_horse(board, x, y, horse_position):
    board[x][y] = horse_position
    if horse_position >= board_side ** 2:
        for line in board:
            print(line)
        sys.exit()
    elif horse_position <= board_side ** 2:
        for i in range(8):
            # Двигаю коняшку
            new_pos_x = x + move_x[i]
            new_pos_y = y + move_y[i]
            # Проверяю возможен ли ход
            if test_move(new_pos_x, new_pos_y) and board[new_pos_x][new_pos_y] == 0:
                move_fucking_horse(board, new_pos_x, new_pos_y, horse_position + 1)
        board[x][y] = 0


if __name__ == '__main__':
    # Создаю доску
    board_side = 7
    board = [[0 for x in range(board_side)] for y in range(board_side)]
    horse_position = 1
    move_fucking_horse(board, 0, 0, horse_position)
