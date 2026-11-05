"""Задача 18. Аттракцион: вернуть места в исходный порядок обменами строк и столбцов."""

import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    rows, cols = data[0], data[1]
    pos = 2
    seats = []
    for _ in range(rows):
        seats.append(data[pos:pos + cols])
        pos += cols

    operations = []

    # В каждом ряду все номера относятся к одному исходному ряду.
    for target_row in range(rows):
        wanted_original_row = target_row
        current_row = target_row
        while (seats[current_row][0] - 1) // cols != wanted_original_row:
            current_row += 1

        if current_row != target_row:
            seats[target_row], seats[current_row] = seats[current_row], seats[target_row]
            operations.append(("R", target_row + 1, current_row + 1))

    # После восстановления рядов первая строка показывает порядок исходных столбцов.
    for target_col in range(cols):
        current_col = target_col
        while (seats[0][current_col] - 1) % cols != target_col:
            current_col += 1

        if current_col != target_col:
            for row in range(rows):
                seats[row][target_col], seats[row][current_col] = (
                    seats[row][current_col], seats[row][target_col]
                )
            operations.append(("C", target_col + 1, current_col + 1))

    output = [str(len(operations))]
    for kind, first, second in operations:
        output.append(f"{kind} {first} {second}")
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
