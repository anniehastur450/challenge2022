#!/usr/bin/env python3

import sys
import traceback

def matrix2d(r, c, n):
    return [[n]*c for _ in range(r)]

def Q7(sb):
    ints = [int(x) for x in ' '.join(sb).split()]
    r = ints[0]
    c = ints[1]
    num = ints[2]
    game = matrix2d(r, c, 0)
    for n in range(num):
        i = ints[3 + n * 2]
        j = ints[4 + n * 2]
        game[i][j] = -1  # -1 means mine
        for a in range(-1, 2):  # [-1, 0, 1]
            for b in range(-1, 2):  # [-1, 0, 1]
                ci = i + a
                cj = j + b
                if ci < 0 or cj < 0 or ci >= r or cj >= c:
                    continue
                if game[ci][cj] == -1:
                    continue
                game[ci][cj] += 1
    for i in range(r):
        for j in range(c):
            val = game[i][j]
            print('*' if val == -1 else val, end='')
        print()


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
            Q7(sb)
        except Exception:
            traceback.print_exc()
