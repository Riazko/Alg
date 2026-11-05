"""Задача 9. Вырубка деревьев: оставшиеся деревья должны образовать АП."""

import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]  # Всего деревьев и сколько должно остаться.

    if m == 0:
        # Единственный вариант: срубить все деревья.
        answer = 1
    elif m == 1:
        # Любое одно дерево подходит: соседних расстояний нет.
        answer = n
    else:
        # Для шага d первый ствол можно выбрать на n-(m-1)*d местах.
        max_step = (n - 1) // (m - 1)
        answer = 0
        for step in range(1, max_step + 1):
            answer += n - (m - 1) * step

    print(answer)


if __name__ == "__main__":
    main()
