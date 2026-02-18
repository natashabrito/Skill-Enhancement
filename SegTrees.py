# 4. The "Range Performance Monitor" (Segment Trees)
# ○ Problem: Design a system for a stock exchange that handles two operations:
# update(index, value) for a stock price and queryMax(L, R) to find the highest price in
# a time range.
# ○ Complexity Requirement: Both operations must be O(\log N).

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, arr)

    def build(self, i, l, r, arr):
        if l == r:
            self.tree[i] = arr[l]
            return

        m = (l + r) // 2

        self.build(i * 2, l, m, arr)
        self.build(i * 2 + 1, m + 1, r, arr)

        self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, i, l, r, idx, val):
        if l == r:
            self.tree[i] = val
            return

        m = (l + r) // 2

        if idx <= m:
            self.update(i * 2, l, m, idx, val)
        else:
            self.update(i * 2 + 1, m + 1, r, idx, val)

        self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, i, l, r, ql, qr):
        if qr < l or ql > r:
            return float('-inf')

        if ql <= l and r <= qr:
            return self.tree[i]

        m = (l + r) // 2

        return max(
            self.query(i * 2, l, m, ql, qr),
            self.query(i * 2 + 1, m + 1, r, ql, qr)
        )

    def update_val(self, idx, val):
        self.update(1, 0, self.n - 1, idx, val)

    def query_max(self, l, r):
        return self.query(1, 0, self.n - 1, l, r)


arr = [5, 2, 6, 3, 1, 7, 4]

st = SegmentTree(arr)

print(st.query_max(1, 5))

st.update_val(3, 10)

print(st.query_max(1, 5))
