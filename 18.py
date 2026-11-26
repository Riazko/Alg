import sys
import time
import tracemalloc


def restore_permutation(permutation, command):
    n = len(permutation)
    pos = [0] * n

    for i in range(n):
        pos[permutation[i]] = i

    operations = []

    for i in range(n):
        j = pos[i]

        if i == j:
            continue

        a = permutation[i]
        b = permutation[j]

        permutation[i], permutation[j] = b, a

        pos[a] = j
        pos[b] = i

        operations.append(f"{command} {i + 1} {j + 1}")

    return operations


def solve(n, m, matrix):
    row_permutation = []
    col_permutation = []

    for i in range(n):
        row = matrix[i]

        row_permutation.append((row[0] - 1) // m)

        if i == 0:
            for value in row:
                col_permutation.append((value - 1) % m)

    operations = []

    operations.extend(
        restore_permutation(row_permutation, "R")
    )

    operations.extend(
        restore_permutation(col_permutation, "C")
    )

    result = str(len(operations))

    if operations:
        result += '\n' + '\n'.join(operations)

    return result


def main():
    read = sys.stdin.buffer.readline

    n, m = map(int, read().split())

    matrix = [
        list(map(int, read().split()))
        for _ in range(n)
    ]

    start_time = time.perf_counter()

    result = solve(n, m, matrix)

    end_time = time.perf_counter()

    tracemalloc.start()

    memory_result = solve(n, m, matrix)

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
