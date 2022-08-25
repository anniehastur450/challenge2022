#!/usr/bin/env python3

import sys
import traceback

def longest_seq(a, b):
    # pure algorithm implementation
    maxCount = 0
    for i in range(len(a)):
        j = 0
        while i + j < len(a) and a[i + j] == b[j % len(b)]:
            j += 1
        maxCount = max(maxCount, j // len(b))  # int divison
    return maxCount

def Q4(sb):
    STR = sb[0]
    DNA = sb[1]
    suspects = sb[2:]
    try:
        index = suspects.index(DNA)
    except ValueError:
        print(0)
        print(0)
        return
    print(index + 1)
    print(longest_seq(DNA, STR))


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
            Q4(sb)
        except Exception:
            traceback.print_exc()
