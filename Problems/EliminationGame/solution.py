class Solution:

    def last_remaining(self, n):
        head = 1
        remaining = n
        is_forward = True
        step = 1

        while remaining > 1:

            if is_forward or remaining % 2 == 1:
                head += step

            remaining = remaining // 2
            step *= 2
            is_forward = not is_forward

        return head