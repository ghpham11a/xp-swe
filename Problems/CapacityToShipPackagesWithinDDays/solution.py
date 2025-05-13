class Solution:
    
    def ship_within_days(self, weights, days):
        # Lower bound: the heaviest package (at least this much capacity is needed)
        lo = max(weights)
        # Upper bound: the total weight (worst case: ship everything in one day)
        hi = sum(weights)

        # Initialize the answer with the upper bound
        output = hi

        # Binary search for the minimal valid capacity
        while lo <= hi:
            # Try a candidate capacity (midpoint)
            capacity = lo + (hi - lo) // 2

            # If it's possible to ship within `days` using this capacity
            if self.can_ship(weights, days, capacity):
                output = min(output, capacity)  # Update result to smaller capacity
                hi = capacity - 1               # Try to find an even smaller one
            else:
                lo = capacity + 1               # Need more capacity to meet the days limit

        return output

    def can_ship(self, weights, days, capacity):
        # Simulate shipping process with given capacity
        curr_days = 1  # Start with day 1
        curr_cap = capacity  # Remaining capacity for the current day

        for wt in weights:
            # If current package can't fit today, increment the day count
            if curr_cap - wt < 0:
                curr_days += 1     # Move to next day
                curr_cap = capacity  # Reset ship capacity
            curr_cap -= wt  # Load the package

        # Return True if we can ship everything within allowed number of days
        return curr_days <= days