"""Задача 21. Сортировка участников heapsort по трём критериям."""

import sys


def is_worse(first, second):
    """True, если first должен стоять после second в итоговом списке."""
    if first[1] != second[1]:
        return first[1] < second[1]       # Меньше решённых задач — ниже.
    if first[2] != second[2]:
        return first[2] > second[2]       # При равенстве задач больший штраф — ниже.
    return first[0] > second[0]           # При равенстве метрик позже по алфавиту — ниже.


def sift_down(heap, root, end):
    """Восстанавливает max-heap по отношению «хуже» в полуинтервале [0, end)."""
    while True:
        left = 2 * root + 1
        if left >= end:
            return

        worst = left
        right = left + 1
        if right < end and is_worse(heap[right], heap[left]):
            worst = right

        if not is_worse(heap[worst], heap[root]):
            return

        heap[root], heap[worst] = heap[worst], heap[root]
        root = worst


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    participants = []
    pos = 1
    for _ in range(n):
        login = tokens[pos].decode()
        solved = int(tokens[pos + 1])
        penalty = int(tokens[pos + 2])
        pos += 3
        participants.append((login, solved, penalty))

    # Строим кучу снизу вверх; её вершина — худший участник.
    for root in range(n // 2 - 1, -1, -1):
        sift_down(participants, root, n)

    # Переносим худшего в конец; в результате список будет от лучшего к худшему.
    for end in range(n - 1, 0, -1):
        participants[0], participants[end] = participants[end], participants[0]
        sift_down(participants, 0, end)

    sys.stdout.write("\n".join(person[0] for person in participants))


if __name__ == "__main__":
    main()
