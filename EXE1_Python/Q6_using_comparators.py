#!/usr/bin/env python3

import sys
import traceback
import calendar
import functools

MONTHS = calendar.month_name[1:]  # calendar.month_name is len 13 [1..12]

class Person:
    def __init__(self, id):
        self.id = id
        self.ptr = 0
        YY = self.readInt(2)
        if YY > 20:
            YY += 1900
        else:
            YY += 2000
        self.YY = YY
        self.MM = self.readInt(2)
        self.DD = self.readInt(2)
        self.ptr += 1
        self.PB = self.readInt(2)
        self.ptr += 1
        self.sss = self.readInt(3)
        self.G = self.readInt(3)

    def readInt(self, count):
        a, b = self.ptr, self.ptr + count
        self.ptr += count
        return int(self.id[a:b])

    def __str__(self):
        # :02 to print 2-digit DD
        return f'{self.id} {self.DD:02} {MONTHS[self.MM-1]}' + \
            f" {self.YY} {'Female' if self.G % 2 == 0 else 'Male'}"

def compare(a, b):  # simulate compare() that in other languages
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def comparator_of_comparing(f):
    return lambda x, y: compare(f(x), f(y))

def Q6(sb):
    ids = []
    sortby = []
    for s in sb:
        if s[0] in '0123456789;':
            ids.append(s)
        else:
            sortby.append(s)
    personList = [Person(x) for x in ''.join(ids).replace(' ', '').split(';')]
    """
    Birthdate
    BirthYear
    BirthMonth
    BirthDay
    GenderwithMalefirst
    GenderwithFemalefirst
    """
    # using comparators which appear the most in other languages
    dict = {
        'Birthdate': comparator_of_comparing(lambda x: x.YY * 10000 + x.MM * 100 + x.DD),
        'BirthYear': comparator_of_comparing(lambda x: x.YY),
        'BirthMonth': comparator_of_comparing(lambda x: x.MM),
        'BirthDay': comparator_of_comparing(lambda x: x.DD),
        'GenderwithMalefirst': comparator_of_comparing(lambda x: 1 - x.G % 2),  # odd first
        'GenderwithFemalefirst': comparator_of_comparing(lambda x: x.G % 2),  # even first
    }
    comparators = []
    sortby = ''.join(sortby).replace(' ', '')
    for i in range(3):
        found = False
        for key, cmp in dict.items():
            if sortby.startswith(key):
                sortby = sortby[len(key):]  # substring
                comparators.append(cmp)
                found = True
                break
        if not found:
            raise RuntimeError(f'i={i} "{sortby}" no match')
    def compare_person(x, y):
        c = 0
        for cmp in comparators:
            c = cmp(x, y)
            if c != 0:
                return c
        return c
    personList.sort(key=functools.cmp_to_key(compare_person))
    for p in personList:
        print(p)


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
            Q6(sb)
        except Exception:
            traceback.print_exc()
