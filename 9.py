import sys
import time
import tracemalloc


def solve(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    if m > n:
        return 0

    d = (n - 1) // (m - 1)

    return d * n - (m - 1) * d * (d + 1) // 2


def main():
    n, m = map(int, input().split())

    start_time = time.perf_counter()

    result = solve(n, m)

    end_time = time.perf_counter()

    print(result)

    tracemalloc.start()
    memory_result = solve(n, m)
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\n--- Статистика ---", file=sys.stderr)
    print(
        f"Время выполнения алгоритма: "
        f"{end_time - start_time:.8f} секунд",
        file=sys.stderr
    )
    print(
        f"Текущая память: {current_memory / 1024:.16f} КБ",
        file=sys.stderr
    )
    print(
        f"Пиковая память: {peak_memory / 1024:.16f} КБ",
        file=sys.stderr
    )


if __name__ == "__main__":
    main()
