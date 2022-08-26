#!/usr/bin/env python3

import sys
import traceback

def mapped(a, b):
    return 2**a * 3**b

class RES:
    def __init__(self):
        self.count = 0

def f(res, n, a, minB):
    # choose [a] and [minB..(until too large)] for this number
    # and pass [0..a-1] and [b+1] for next number
    # return true/false of "should we continue?"

    b = minB
    k = mapped(a, b)
    while k < n:
        nextA = a - 1
        while nextA >= 0:
            f(res, n - k, nextA, b + 1)
            nextA -= 1
        b += 1
        k = mapped(a, b)
    if k == n:
        res.count += 1
    return b != 0

def Q11(sb):
    # instead of finding how many ways,
    # we build the number from 0,
    # add one step by one step,
    # until the number is larger than the target

    # condition 1 is important: None of the summands can divide any of the other summands.

    # consider 2^a * 3^b and 2^c * 3^d
    # if a >= c && b >= d, then condition 1 must violate
    # question: is diff set of (a, b) map to unique numer? ans: yes
    n = int(sb[0])

    res = RES()
    a = 0
    while f(res, n, a, 0):
        a += 1
    print(res.count)


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
            Q11(sb)
        except Exception:
            traceback.print_exc()
