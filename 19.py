import sys
import time
import tracemalloc


def solve(n, capacity, commands):
    data = [0] * capacity

    head = 0
    size = 0

    answers = []

    for command in commands:
        operation = command[0]

        if operation == b'push_back':
            if size == capacity:
                answers.append("error")
                continue

            value = int(command[1])

            index = (head + size) % capacity
            data[index] = value

            size += 1

        elif operation == b'push_front':
            if size == capacity:
                answers.append("error")
                continue

            value = int(command[1])

            head = (head - 1) % capacity
            data[head] = value

            size += 1

        elif operation == b'pop_front':
            if size == 0:
                answers.append("error")
                continue

            answers.append(str(data[head]))

            head = (head + 1) % capacity
            size -= 1

        elif operation == b'pop_back':
            if size == 0:
                answers.append("error")
                continue

            index = (head + size - 1) % capacity

            answers.append(str(data[index]))

            size -= 1

    return '\n'.join(answers)


def main():
    read = sys.stdin.buffer.readline

    n = int(read())
    capacity = int(read())

    commands = [
        read().split()
        for _ in range(n)
    ]

    start_time = time.perf_counter()

    result = solve(n, capacity, commands)

    end_time = time.perf_counter()

    tracemalloc.start()

    memory_result = solve(n, capacity, commands)

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    sys.stdout.write(result)

    print("\n\n--- Статистика ---", file=sys.stderr)
    print(
        f"Время выполнения: {end_time - start_time:.8f} секунд",
        file=sys.stderr
    )
    print(
        f"Текущая память: {current_memory / 1024:.6f} КБ",
        file=sys.stderr
    )
    print(
        f"Пиковая память: {peak_memory / 1024:.6f} КБ",
        file=sys.stderr
    )


if __name__ == "__main__":
    main()
