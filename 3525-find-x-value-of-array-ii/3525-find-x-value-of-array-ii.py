class SegmentTree:
    MAXK = 6

    def __init__(self, nums, k):
        self.k = k
        self.n = len(nums)
        self.tree = [[0] * self.MAXK for _ in range(4 * self.n + 5)]
        self._build(nums, 1, 0, self.n - 1)

    def _make_leaf(self, node, value):
        self.tree[node] = [0] * self.MAXK

        remainder = value % self.k
        self.tree[node][remainder] = 1
        self.tree[node][self.k] = remainder

    def _merge(self, left, right):
        result = [0] * self.MAXK

        mul_left = left[self.k]
        mul_right = right[self.k]

        for x in range(self.k):
            result[x] = left[x]

        for x in range(self.k):
            remainder = (mul_left * x) % self.k
            result[remainder] += right[x]

        result[self.k] = (mul_left * mul_right) % self.k

        return result

    def _maintain(self, node):
        self.tree[node] = self._merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def _build(self, nums, node, left, right):
        if left == right:
            self._make_leaf(node, nums[left])
            return

        mid = (left + right) // 2

        self._build(nums, node * 2, left, mid)
        self._build(nums, node * 2 + 1, mid + 1, right)

        self._maintain(node)

    def update(self, node, left, right, index, value):
        if left == right:
            self._make_leaf(node, value)
            return

        mid = (left + right) // 2

        if index <= mid:
            self.update(node * 2, left, mid, index, value)
        else:
            self.update(node * 2 + 1, mid + 1, right, index, value)

        self._maintain(node)

    def query(self, node, left, right, query_left, query_right):
        if query_left <= left and right <= query_right:
            return self.tree[node]

        mid = (left + right) // 2

        if query_right <= mid:
            return self.query(
                node * 2,
                left,
                mid,
                query_left,
                query_right
            )

        if query_left > mid:
            return self.query(
                node * 2 + 1,
                mid + 1,
                right,
                query_left,
                query_right
            )

        left_result = self.query(
            node * 2,
            left,
            mid,
            query_left,
            query_right
        )

        right_result = self.query(
            node * 2 + 1,
            mid + 1,
            right,
            query_left,
            query_right
        )

        return self._merge(left_result, right_result)


class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        seg = SegmentTree(nums, k)
        answer = [0] * len(queries)

        for i, query in enumerate(queries):
            index, value, start, x = query

            seg.update(1, 0, n - 1, index, value)

            result = seg.query(1, 0, n - 1, start, n - 1)
            answer[i] = result[x]

        return answer