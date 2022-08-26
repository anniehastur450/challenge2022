#!/usr/bin/env python3

import sys
import traceback

class Polynomial:
    def __init__(self):
        self.coefficients = []  # a_i = coefficients[i]

    def f(self, x):
        ans = 0
        for i, c in enumerate(self.coefficients):
            ans += c * x**i
        return ans

    def differentiate(self):
        res = Polynomial()
        for n in range(1, len(self.coefficients)):
            res.coefficients.append(self.coefficients[n] * n)
        return res

def findRoot(p, diff_p, q_j, s_j):
    a = findRoot0(p, diff_p, (q_j + s_j) / 2)
    if q_j <= a <= s_j:
        return a
    a = findRoot0(p, diff_p, q_j)
    if q_j <= a <= s_j:
        return a
    a = findRoot0(p, diff_p, s_j)
    if q_j <= a <= s_j:
        return a
    return float('nan')

def findRoot0(p, diff_p, x_1):
    error = 0.000_000_001
    x_2 = x_1 - p.f(x_1) / diff_p.f(x_1)
    while (abs(x_2 - x_1) > error):
        x_1 = x_2
        x_2 = x_1 - p.f(x_1) / diff_p.f(x_1)
    return x_2

def Q12(sb):
    #  this is a typical newton method question,
    #  but i have never touch that before

    #  to implement it myself, one gif speak it all:
    #  https://commons.wikimedia.org/wiki/File:NewtonIteration_Ani.gif
    n = int(sb[0])
    p = Polynomial()
    for i in range(n+1):
        p.coefficients.append(float(sb[n + 1 - i]))
    diff_p = p.differentiate()
    m = int(sb[n + 2])
    for j in range(m):
        q_j = float(sb[n + 3 + j * 2])
        s_j = float(sb[n + 4 + j * 2])
        print('%.6f' % findRoot(p, diff_p, q_j, s_j))


if __name__ == '__main__':
    """Verify test cases easily
    1. run the program
    2. paste test case to stdin
    3. press double Enter
    4. continue pasting next test case
    """
    do_next = True
    while do_next:
        try:
            do_next = False  # do_next won't set if encounter EOF
            sb = []
            for line in sys.stdin:  # s = data + '\n'
                line = line.rstrip('\r\n')
                if line:  # check str not empty
                    sb.append(line)
                elif sb:  # check list not empty
                    do_next = True
                    break
            Q12(sb)
        except Exception:
            traceback.print_exc()
