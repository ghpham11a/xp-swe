class Solution:

    def find_nth_digit(self, n: int) -> int:
        
        if n <= 9:
            return n

        n_digits = 1
        base = 1

        while n >= 9 * base * n_digits:
            n -= 9 * base * n_digits
            n_digits += 1
            base *= 10
        
        if n == 0:
            return 9

        number = base + (n - 1) // n_digits
        digit_index = (n - 1) % n_digits
        
        return int(str(number)[digit_index])