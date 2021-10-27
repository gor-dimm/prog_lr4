#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6. Создайте процедуру, печатающую все возможные представления натурального числа в
# виде суммы других натуральных чисел.


n = 6


def step(n, L):
    if n != 0:
        if n >= L[len(L) - 1]:
            for i in range(max(1, L[len(L) - 1]), n + 1):
                step(n - i, L + [i])

    else:
        print(L[1], end="")
        for i in L[2:]:
            print('+{0}'.format(i), end="")
        print()


step(n, [0])
