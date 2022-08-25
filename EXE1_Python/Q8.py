#!/usr/bin/env python3

import sys
import traceback
import math

def round_2DecimalPlaces(d):
    # round(2.235, 2) gives us 2.23 instead of 2.24
    # see https://docs.python.org/3/library/functions.html#round

    # and round(x) in python3 is "round half to even"
    # e.g. round(1.5) -> 2, round(2.5) -> 2, round(3.5) -> 4
    # see https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior
    # we use math.copysign(int(abs(x) + .5), x) instead
    return math.copysign(int(abs(d * 100) + .5), d) / 100

def Q8_2(nums):
    prev = 0.0
    count = 0
    for d in nums:
        if d is None:
            count += 1
        else:
            if count != 0:
                for c in range(count):
                    res = prev + (d - prev) / (count + 1) * (c + 1)
                    print('%.2f' % round_2DecimalPlaces(res))
            count = 0
            prev = d

def Q8(sb):
    count = int(sb[0])
    nums = []
    for i in range(count):
        s = sb[i + 1]
        if '#' == s:
            nums.append(None)
        else:
            nums.append(float(s))
    Q8_2(nums)


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
            Q8(sb)
        except Exception:
            traceback.print_exc()
