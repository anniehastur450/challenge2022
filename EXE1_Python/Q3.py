#!/usr/bin/env python3

import sys
import traceback
import re

def Q3(sb):
    # is regex too cheat?
    ans = sorted(set(x.upper() for x in re.findall("[a-zA-Z’']+", ' '.join(sb))))
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
