import random

grid_is_valid = False
solution = []


def make_grid():
    x = 10
    grid = [[0] * x for y in range(x)]
    for i in range(1, 10):
        for j in range(1, 10):
            grid[i][j] = random.randint(1, 9)
    return grid


def check_rows(puzzle):
    for i in range(1, 10):
        row_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(1, 10):
            row_counter[puzzle[i][j]-1] += 1
        for k in row_counter:
            if row_counter[k] != 1:
                return False
    return True


def check_columns(puzzle):
    for j in range(1, 10):
        column_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, 10):
            column_counter[puzzle[i][j]-1] += 1
        for k in column_counter:
            if column_counter[k] != 1:
                return False
    return True


def check_upper_left(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 4):
        for j in range(1, 4):
            count[puzzle[i][j]-1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_upper_center(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 4):
        for j in range(4, 7):
            count[puzzle[i][j]-1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_upper_right(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 4):
        for j in range(7, 10):
            count[puzzle[i][j] - 1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_middle_left(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(4, 7):
        for j in range(1, 4):
            count[puzzle[i][j]-1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_middle_center(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(4, 7):
        for j in range(4, 7):
            count[puzzle[i][j]-1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_middle_right(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(4, 7):
        for j in range(7, 10):
            count[puzzle[i][j] - 1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_lower_left(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(7, 10):
        for j in range(1, 4):
            count[puzzle[i][j]-1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_lower_center(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(7, 10):
        for j in range(4, 7):
            count[puzzle[i][j]-1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_lower_right(puzzle):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(7, 10):
        for j in range(7, 10):
            count[puzzle[i][j] - 1] += 1
    for k in count:
        if count[k] != 1:
            return False
    return True


def check_grid(puzzle):
    if check_rows(puzzle) is False:
        return False
    elif check_columns(puzzle) is False:
        return False
    elif check_upper_left(puzzle) is False:
        return False
    elif check_upper_center(puzzle) is False:
        return False
    elif check_upper_right(puzzle) is False:
        return False
    elif check_middle_left(puzzle) is False:
        return False
    elif check_middle_center(puzzle) is False:
        return False
    elif check_middle_right(puzzle) is False:
        return False
    elif check_lower_left(puzzle) is False:
        return False
    elif check_lower_center(puzzle) is False:
        return False
    elif check_lower_right(puzzle) is False:
        return False
    else:
        return True


while grid_is_valid is False:
    solution = make_grid()
    grid_is_valid = check_grid(solution)

for line in solution:
    print(line)
