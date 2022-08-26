#!/usr/bin/env python3

import sys
import traceback
import heapq

class MaxHeap:
    """A object-oriented max heap implementation by wrapping python heapq module
    """
    def __init__(self):
        self.heap = []

    def push(self, num):
        heapq.heappush(self.heap, -num)  # heapq is min heap

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]

    def __len__(self):  # define __len__ for __bool__ which is for emptiness checking
        return len(self.heap)

class Order:
    def __init__(self, s):
        self.name = None
        self.queue = MaxHeap()
        self.totalCount = 0
        self.waitedMinutes = 0

        s2 = s.split('#')
        self.name = s2[0]
        for s3 in s2[1].split('%'):
            count = int(s3.split(':')[1])
            self.queue.push(count)
            self.totalCount += count

    def doWait(self):
        if self.totalCount == 0:
            return
        self.waitedMinutes += 5

class Cook:
    def __init__(self):
        self.cookingFor = None
        self.remainingCount = 0

    def acquireFood(self, orders):
        if self.remainingCount != 0:
            return
        for o in orders:
            if o.queue:  # if queue not empty
                self.cookingFor = o
                self.remainingCount = o.queue.pop()
                return

    def cook(self):
        if self.remainingCount != 0:
            self.remainingCount -= 1
            self.cookingFor.totalCount -= 1

def needWaiting(orders):
    for o in orders:
        if o.totalCount > 0:
            return True
    return False

def Q9(sb):
    s = ''.join(sb).replace(' ', '')
    orders = [Order(substr) for substr in s.split(';')]
    # process order now
    cooks = [Cook() for _ in range(3)]
    qq = 0
    while needWaiting(orders):
        for c in cooks:
            c.acquireFood(orders)

        for o in orders:
            o.doWait()
        for c in cooks:
            c.cook()

        qq += 1
        if qq > 1000:
            raise RuntimeError('error: never ends...')

    for o in orders:
        hr = 10
        min = 0
        min += o.waitedMinutes
        hr += min // 60  # int divison
        min %= 60
        print('%s can collect food at %02d:%02d' % (o.name, hr, min))


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
            Q9(sb)
        except Exception:
            traceback.print_exc()
