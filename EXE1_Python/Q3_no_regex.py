#!/usr/bin/env python3

import sys
import traceback

def Q3(sb):
    def is_in(char): # True if in [a-zA-Z’']
        return char in "’'" or \
            'a' <= char <= 'z' or \
            'A' <= char <= 'Z'  # python syntax, chained comparison
    s = ' '.join(sb)
    j = 0
    ans = set()
    for i, c in enumerate(s):
        if not is_in(c):
            if i - j > 0:  # if substr length > 0
                ans.add(s[j:i].upper())
            j = i + 1
    ans = sorted(ans)
    print(len(ans))
    for s in ans:
        print(s)


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
            Q3(sb)
        except Exception:
            traceback.print_exc()
