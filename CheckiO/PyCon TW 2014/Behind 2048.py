# http://www.checkio.org/mission/simple2048

def move2048(state, move):

    def rotate(matrix, direction, times):
        for _ in range(times):
            # clockwise
            if direction == 'cw':
                matrix = list(map(list, zip(*matrix[::-1])))

            # counter clockwise
            if direction == 'ccw':
                matrix = list(map(list, zip(*matrix)))[::-1]

        return matrix


    def left_merge_row(row):
        # [2, 0, 2, 2]
        # [2, 2, 2, 0]
        # [4, 2, 0, 0]

        # move non-zero number to left
        new_row = [x for x in row if x] + [0]*row.count(0)

        # left merge number
        for i in range(len(new_row)-1):
            if new_row[i] == new_row[i+1]:
                new_row[i] *= 2
                new_row.pop(i+1)
                new_row.append(0)

        return new_row


    def add_new_tile(matrix):
        flatten_matrix = sum(matrix, [])

        if 0 in flatten_matrix:
            # reverse the flatten_matrix to get the index of the last empty tile
            new_tile_index = len(flatten_matrix)-1 - flatten_matrix[::-1].index(0)
            flatten_matrix[new_tile_index] = 2

        # repackage flatten_matrix to nxn matrix
        return list(map(list, zip(*[iter(flatten_matrix)]*len(matrix))))


    rotate_times = {
        'left': 0,
        'up': 1,
        'right': 2,
        'down': 3
    }

    # 1. counter clockwise rotate
    # 2. merge rows
    # 3. clockwise rotate
    # 4. add new tile
    new_state = add_new_tile(
        rotate(
            list(map(left_merge_row, rotate(state, 'ccw', rotate_times[move]))),
            'cw',
            rotate_times[move]
        )
    )

    if 2048 in sum(new_state, []):
        return [list('UWIN')]*4
    elif all(sum(new_state, [])):
        # no 0 in new_state
        return [list('GAME'), list('OVER')]*2
    else:
        return new_state


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert move2048([[0, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 2, 0, 0]], 'up') == [[0, 4, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 2]], "Start. Move Up!"
    assert move2048([[4, 0, 0, 0],
                     [0, 4, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 8, 8]], 'right') == [[0, 0, 0, 4],
                                                 [0, 0, 0, 4],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 2, 16]], "Simple right"
    assert move2048([[2, 0, 2, 2],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'right') == [[0, 0, 2, 4],
                                                 [0, 0, 4, 8],
                                                 [0, 8, 16, 16],
                                                 [0, 0, 0, 2]], "Three merging"
    assert move2048([[256, 0, 256, 4],
                     [16, 8, 8, 0],
                     [32, 32, 32, 32],
                     [4, 4, 2, 2]], 'right') == [[0, 0, 512, 4],
                                                 [0, 0, 16, 16],
                                                 [0, 0, 64, 64],
                                                 [0, 2, 8, 4]], "All right"
    assert move2048([[4, 4, 0, 0],
                     [0, 4, 1024, 0],
                     [0, 256, 0, 256],
                     [0, 1024, 1024, 8]], 'down') == [['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N']], "We are the champions!"
    assert move2048([[2, 4, 8, 16],
                     [32, 64, 128, 256],
                     [512, 1024, 2, 4],
                     [8, 16, 32, 64]], 'left') == [['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R'],
                                                   ['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R']], "Nobody moves!"
