#!/usr/bin/env python3

import sys
import traceback

def getLowest(nums, lookup, set_of_indexes):
    key = frozenset(set_of_indexes)  # set must be converted to frozenset to be dict key
    if key not in lookup:
        # find lowest of these 4 indexes
        sum0 = sum([nums[x] for x in key])
        lowest = None
        for x in key:
            sum1 = sum0 - nums[x]
            sum1 += nums[x] / (2 if sum1 >= 80 else 1)
            if lowest is None or sum1 < lowest:
                lowest = sum1
        lookup[key] = lowest
    return lookup[key]

class DPDATA:
    def __init__(self, nums):
        self.nums = nums
        self.lookup = {}
        self.lowest = None
        self.a = set(range(8))
        self.b = set()

    def updateLowest(self):
        curr = getLowest(self.nums, self.lookup, self.a) + \
            getLowest(self.nums, self.lookup, self.b)
        if self.lowest is None or curr < self.lowest:
            self.lowest = curr

def dp(DP, st):
    if len(DP.a) == 4:
        DP.updateLowest()
        return
    for i in range(st, 8):
        DP.a.remove(i)
        DP.b.add(i)
        dp(DP, i+1)
        DP.b.remove(i)
        DP.a.add(i)

def Q10(sb):
    # brute force 8 dishes will need 8! = 40320
    # brute force first 4 dishes first only need 8*7*6*5 + 4*3*2*1
    #     which = 1704
    # choose 3 from 8 first will need 8C3 * 5 + 4C3 * 1
    #     which = 284
    # or 8C3 * 5 * 4C3 * 1 = 1120

    # do (8 choose 4 * 4 choose 3) + 4 choose 3 using dict
    #     which = 284
    nums = [float(s) for s in sb]
    DP = DPDATA(nums)
    dp(DP, 0)
    print('%.2f' % DP.lowest)


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
