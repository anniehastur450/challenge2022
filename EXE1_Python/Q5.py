#!/usr/bin/env python3

import sys
import traceback

def swap(s, a, b):
    s[a], s[b] = s[b], s[a]

def do2opt(s, index1, index2):
    if index1 > index2:
        do2opt(s, index2, index1)
        return
    else:
        i = 0
        while i < (index2 - index1 + 1) // 2:
            # swap index1 + i, index2 - i
            swap(s, index1 + i, index2 - i)
            i += 1

def Q5(sb):
    count = int(sb[0])
    s = list('abcdefgha')
    for i in range(count):
        index1 = s.index(sb[i + 1][0])
        index2 = s.index(sb[i + 1][1])
        do2opt(s, index1, index2)
    print(''.join(s))


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
            Q5(sb)
        except Exception:
            traceback.print_exc()
