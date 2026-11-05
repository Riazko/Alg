"""Задача 17. Охрана: проверить сплошное покрытие и незаменимость каждого поста."""

import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    tests = data[0]
    pos = 1
    answers = []

    for _ in range(tests):
        guards = data[pos]
        pos += 1

        # Временные промежутки пронумерованы от 1 до 10000.
        # Для визита (A, B] охранник покрывает интервалы A+1..B.
        difference = [0] * 10002
        intervals = []
        for _ in range(guards):
            start, finish = data[pos], data[pos + 1]
            pos += 2
            intervals.append((start, finish))
            difference[start + 1] += 1
            difference[finish + 1] -= 1

        coverage = 0
        single_prefix = [0] * 10002
        safe = True
        for interval in range(1, 10001):
            coverage += difference[interval]
            # База должна быть под охраной хотя бы одного человека всё время.
            if coverage == 0:
                safe = False
            # Префиксное число отрезков, где дежурит ровно один охранник.
            single_prefix[interval] = single_prefix[interval - 1] + (coverage == 1)

        # У каждого охранника должен быть собственный отрезок: без него там станет пусто.
        for start, finish in intervals:
            if single_prefix[finish] - single_prefix[start] == 0:
                safe = False
                break

        answers.append("Accepted" if safe else "Wrong Answer")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
