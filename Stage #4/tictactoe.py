def make_field(cells):
    for i in range(len(cells)):
        if cells[i] == "_":
            cells[i] = " "
    print('---------')
    for i in range(0, 7, 3):
        print("| {} {} {} |".format(cells[i], cells[i+1], cells[i+2]))
    print('---------')


def main():
    active = True
    cells = list(input('Enter cells: > '))
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
                        cells[move_patterns.index(cell)] = 'X'
                        make_field(cells)
                        active = False
        except ValueError:
            print('You should enter numbers!')
            continue

        except IndexError:
            print('You should enter numbers!')
            continue


if __name__ == '__main__':
    main()
