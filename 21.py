import sys
import time
import tracemalloc


def is_worse(a, b):
    if a[1] != b[1]:
        return a[1] < b[1]

    if a[2] != b[2]:
        return a[2] > b[2]

    return a[0] > b[0]


def sift_down(arr, root, size):
    while True:
        largest = root

        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and is_worse(arr[left], arr[largest]):
            largest = left

        if right < size and is_worse(arr[right], arr[largest]):
            largest = right

        if largest == root:
            break

        arr[root], arr[largest] = arr[largest], arr[root]

        root = largest


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end)


def solve(participants):
    heap_sort(participants)

    output = [person[0] for person in participants]

    return '\n'.join(output)


def main():
    read = sys.stdin.buffer.readline

    n = int(read())

    participants = []

    for _ in range(n):
        login, solved, penalty = read().split()

        participants.append((
            login.decode(),
            int(solved),
            int(penalty)
        ))

    start_time = time.perf_counter()

    result = solve(participants.copy())

    end_time = time.perf_counter()

    tracemalloc.start()

    memory_participants = participants.copy()
    memory_result = solve(memory_participants)

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
