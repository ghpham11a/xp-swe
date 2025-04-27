class Solution:
    def isHappy(self, n: int) -> bool:
        slow_runner = n
        fast_runner = self.get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = self.get_next(slow_runner)
            fast_runner = self.get_next(self.get_next(fast_runner))
        return fast_runner == 1

    def get_next(self, number: int) -> int:
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum