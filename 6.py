import sys
import time
import tracemalloc


def solve(n, m, mod, coefficients, arguments):
    answers = []

    for x in arguments:
        result = 0

        for a in coefficients:
            result = (result * x + a) % mod

        answers.append(str(result))

    return "\n".join(answers)


def main():
    read = sys.stdin.buffer.readline

    n, m, mod = map(int, read().split())

    coefficients = []

    while len(coefficients) < n + 1:
        coefficients.extend(map(int, read().split()))

    arguments = []

    while len(arguments) < m:
        arguments.extend(map(int, read().split()))

    start_time = time.perf_counter()

    result = solve(n, m, mod, coefficients, arguments)

    end_time = time.perf_counter()

    tracemalloc.start()

    memory_result = solve(n, m, mod, coefficients, arguments)

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
