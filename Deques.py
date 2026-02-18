from collections import deque

class StreamingMax:
    def __init__(self, k):
        self.k = k
        self.dq = deque()
        self.i = 0

    def add(self, value):

        while self.dq and self.dq[-1][0] < value:
            self.dq.pop()

        self.dq.append((value, self.i))

        if self.dq[0][1] <= self.i - self.k:
            self.dq.popleft()

        self.i += 1

        if self.i >= self.k:
            return self.dq[0][0]
        return None
sm = StreamingMax(3)

data = [10, 5, 2, 7, 8, 7]

for x in data:
    print(sm.add(x))