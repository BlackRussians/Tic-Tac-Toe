def make_field(cells):
    for i in range(len(cells)):
        if cells[i] == "_":
            cells[i] = " "
    print('---------')
    for i in range(0, 7, 3):
        print("| {} {} {} |".format(cells[i], cells[i+1], cells[i+2]))
    print('---------')


def chk_field(cells):
    global active
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
        active = 0
    elif x_win == 1:
        print('X wins')
        active = 0
    elif o_win == 1:
        print('O wins')
        active = 0
    elif cells.count('X') >= 5 and cells.count('X') >= 5:
        print('Draw')
        active = 0


def main():
    turns = 0
    cells = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    make_field(cells)
    move_patterns = [(1, 3), (2, 3), (3, 3), (1, 2), (2, 2), (3, 2), (1, 1), (2, 1), (3, 1)]
    while active:
        try:
            coordinates = tuple(map(int, input("Enter the coordinates: > ").split()))
            if coordinates[0] > 3 or coordinates[1] > 3 or coordinates[0] <= 0 or coordinates[1] <= 0:
                print('Coordinates should be from 1 to 3!')
            for cell in move_patterns:
                if cell == coordinates:
                    if cells[move_patterns.index(cell)] != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        if turns == 0:
                            turns += 1
                            cells[move_patterns.index(cell)] = 'X'
                            make_field(cells)
                        elif turns == 1:
                            turns -= 1
                            cells[move_patterns.index(cell)] = 'O'
                            make_field(cells)
                        chk_field(cells)
        except ValueError:
            print('You should enter numbers!')
            continue

        except IndexError:
            print('You should enter numbers!')
            continue


if __name__ == '__main__':
    active = 1
    main()
