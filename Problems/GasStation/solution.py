class Solution:

    def can_complete_circuit(self, gas, cost):
        # If the total gas is less than the total cost, 
        # it's impossible to complete the circuit.
        if sum(gas) < sum(cost):
            return -1

        total = 0  # Tracks the current balance of gas in the tank
        output = 0  # Candidate starting gas station index

        for i in range(len(gas)):
            # Update total gas in the tank after visiting station i
            total += (gas[i] - cost[i])

            # If the tank becomes negative, 
            # it means we can't reach the next station from the current start
            if total < 0:
                # Reset total gas because we need to start from a new station
                total = 0
                # The next station (i + 1) becomes the new candidate
                output = i + 1

        # After checking all stations, return the valid starting station index
        return output
    
solution = Solution()

assert(solution.can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]) == 3)

print("PASS")