"""Задача 6. Вычисление полинома по модулю."""

import sys


def main():
    # Считываем числа одним массивом: N, M, MOD, коэффициенты и аргументы.
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n, m, mod = values[0], values[1], values[2]
    # Коэффициенты идут от старшего a_N к свободному a_0.
    coefficients = values[3:3 + n + 1]
    arguments = values[3 + n + 1:3 + n + 1 + m]

    answers = []
    for x in arguments:
        # Схема Горнера: ((((a_N*x+a_{N-1})*x+...)*x)+a_0).
        result = coefficients[0] % mod
        for index in range(1, n + 1):
            result = (result * x + coefficients[index]) % mod
        answers.append(str(result))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
