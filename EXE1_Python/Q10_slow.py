#!/usr/bin/env python3

import sys
import traceback

def howMuch(a, b, c, d):
    sum1 = a + b + c
    sum1 += d / 2 if sum1 >= 80 else d
    return sum1

def dp(nums, indexes, do_f):
    if len(indexes) == len(nums):
        do_f(indexes)
    for i in range(len(nums)):
        if i not in indexes:
            indexes.append(i)
            dp(nums, indexes, do_f)
            indexes.pop()

def Q10(sb):
    # brute force 8 dishes will need 8! = 40320
    # brute force first 4 dishes first only need 8*7*6*5 + 4*3*2*1
    #     which = 1704
    # choose 3 from 8 first will need 8C3 * 5 + 4C3 * 1
    #     which = 284

    # just do 8! = 40320, not a big deal
    nums = [float(s) for s in sb]
    lowest = None
    def f(indexes):
        nonlocal lowest
        curr = howMuch(*[nums[x] for x in indexes[0:4]]) + \
            howMuch(*[nums[x] for x in indexes[4:]])
        if lowest is None or curr < lowest:
            lowest = curr
    dp(nums, [], f)
    print('%.2f' % lowest)


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
            Q10(sb)
        except Exception:
            traceback.print_exc()
