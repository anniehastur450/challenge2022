#!/usr/bin/env python3

import sys
import traceback
import calendar
import operator

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
        # those attributes are for: the pythonic way to do it
        self.Birthdate = self.YY * 10000 + self.MM * 100 + self.DD
        self.BirthYear = self.YY
        self.BirthMonth = self.MM
        self.BirthDay = self.DD
        self.GenderwithMalefirst = 1 - self.G % 2
        self.GenderwithFemalefirst = self.G % 2

    def readInt(self, count):
        a, b = self.ptr, self.ptr + count
        self.ptr += count
        return int(self.id[a:b])

    def __str__(self):
        # :02 to print 2-digit DD
        return f'{self.id} {self.DD:02} {MONTHS[self.MM-1]}' + \
            f" {self.YY} {'Female' if self.G % 2 == 0 else 'Male'}"

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
    # the pythonic way to do it
    # see python docs Sorting HOW TO
    # https://docs.python.org/3/howto/sorting.html
    valid_attrs = [
        'Birthdate',
        'BirthYear',
        'BirthMonth',
        'BirthDay',
        'GenderwithMalefirst',
        'GenderwithFemalefirst',
    ]
    attrs = []
    sortby = ''.join(sortby).replace(' ', '')
    for i in range(3):
        found = False
        for attr in valid_attrs:
            if sortby.startswith(attr):
                sortby = sortby[len(attr):]  # substring
                attrs.append(attr)
                found = True
                break
        if not found:
            raise RuntimeError(f'i={i} "{sortby}" no match')
    personList.sort(key=operator.attrgetter(*attrs))
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
