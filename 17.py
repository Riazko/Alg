import sys
import time
import tracemalloc


def solve_case(n, intervals):
    diff = [0] * 10002

    for a, b in intervals:
        diff[a + 1] += 1
        diff[b + 1] -= 1

    coverage = [0] * 10001
    current = 0

    for i in range(1, 10001):
        current += diff[i]
        coverage[i] = current

        if current == 0:
            return False

    for a, b in intervals:
        for i in range(a + 1, b + 1):
            if coverage[i] == 1:
                break
        else:
            return False

    return True


def main():
    k = int(input())
    test_cases = []

    for _ in range(k):
        n, *values = map(int, input().split())
        intervals = []

        while len(values) < 2 * n:
            values.extend(map(int, input().split()))

        for i in range(0, 2 * n, 2):
            intervals.append((values[i], values[i + 1]))

        test_cases.append((n, intervals))

    start_time = time.perf_counter()

    tracemalloc.start()

    answers = []

    for n, intervals in test_cases:
        answers.append(
            "Accepted" if solve_case(n, intervals)
            else "Wrong Answer"
        )

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    end_time = time.perf_counter()

    print('\n'.join(answers))

    print("\n--- Статистика ---", file=sys.stderr)
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
