def chk_field(cells):
    x_win = 0
    o_win = 0
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for a, b, c in win_patterns:
        if (cells[a], cells[b], cells[c]) == ('X', 'X', 'X'):
            x_win += 1
        if (cells[a], cells[b], cells[c]) == ('O', 'O', 'O'):
            o_win += 1

    if x_win > 0 and o_win > 0 or abs(cells.count('X')-cells.count('O')) == 2:
        print('Impossible')
    elif x_win == 1:
        print('X wins')
    elif o_win == 1:
        print('O wins')
    elif cells.count('X') >= 4 and cells.count('X') >= 4:
        print('Draw')
    else:
        print('Game not finished')


def main():
    cells = list(input('Enter cells: > '))
    print('---------')
    for i in range(0, 7, 3):
        print("| {} {} {} |".format(cells[i], cells[i+1], cells[i+2]))
    print('---------')
    chk_field(cells)


if __name__ == '__main__':
    main()
