#!/usr/bin/env python3

import sys
import traceback

def Q1(sb):
    M = int(sb[0])
    N = int(sb[1])
    P = int(sb[2])
    Q = int(sb[3])
    candy = N * M
    ans = 0
    paper = 0
    while candy > 0:
        ans += candy
        paper += candy
        old_candy = candy
        candy = paper // P * Q  # use int divison
        if candy > old_candy:
            raise ValueError('error: inf loop')
        paper %= P
    print(ans)


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
            Q1(sb)
        except Exception:
            traceback.print_exc()
