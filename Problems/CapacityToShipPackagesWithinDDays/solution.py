class Solution:
    
    def ship_within_days(self, weights, days):
        lo = max(weights)
        hi = sum(weights)

        output = hi

        while lo <= hi:
            capacity = lo + (hi - lo) // 2
            if self.can_ship(weights, days, capacity):
                output = min(output, capacity)
                hi = capacity - 1
            else:
                lo = capacity + 1

        return output

    def can_ship(self, weights, days, capacity):
        curr_days = 1
        curr_cap = capacity
        for wt in weights:
            if curr_cap - wt < 0:
                curr_days += 1
                curr_cap = capacity
            curr_cap -= wt
        return curr_days <= days