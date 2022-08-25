#!/usr/bin/env python3

import sys
import traceback

factors = {
    'American Beech':         6,
    'Basswood':               3,
    'Common Horsechestnut':   8,
    'Dogwood':                7,
    'European White Birch':   5,
    'White Fir':            7.5,
}

def Q2(sb):
    try:
        N = int(sb[0])
        if N <= 0:
            raise ValueError
    except ValueError:
        print('You must specify a positive integer number for the number of trees!')
        return
    for i in range(N):
        circum = float(sb[1 + i * 2])
        treeName = sb[2 + i * 2]
        if circum <= 0:
            print(f'The circumference for {treeName} must be greater than 0!')
            continue
        if treeName in factors:
            DBH = circum / 3.141592
            age = DBH * factors[treeName]
            print(f'{treeName} : {circum:.1f} : {age:.1f}')
        else:
            print('Species entered is not available!')


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
            Q2(sb)
        except Exception:
            traceback.print_exc()
