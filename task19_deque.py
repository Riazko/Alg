"""Задача 19. Дек фиксированной вместимости на кольцевом массиве."""

import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    command_count = int(tokens[0])
    capacity = int(tokens[1])
    values = [0] * capacity  # Сам массив хранения дека.
    head = 0                # Индекс первого элемента.
    size = 0                # Текущее число элементов.
    pos = 2
    output = []

    for _ in range(command_count):
        command = tokens[pos].decode()
        pos += 1

        if command == "push_back":
            value = int(tokens[pos])
            pos += 1
            if size == capacity:
                output.append("error")
            else:
                index = (head + size) % capacity
                values[index] = value
                size += 1

        elif command == "push_front":
            value = int(tokens[pos])
            pos += 1
            if size == capacity:
                output.append("error")
            else:
                head = (head - 1) % capacity
                values[head] = value
                size += 1

        elif command == "pop_front":
            if size == 0:
                output.append("error")
            else:
                output.append(str(values[head]))
                head = (head + 1) % capacity
                size -= 1

        else:  # Единственная оставшаяся команда — pop_back.
            if size == 0:
                output.append("error")
            else:
                index = (head + size - 1) % capacity
                output.append(str(values[index]))
                size -= 1

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
