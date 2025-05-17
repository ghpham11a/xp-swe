class Solution:
    def majority_element(self, nums):
        count = 0           # Counter to track the balance of votes
        candidate = None    # Placeholder for the current majority candidate

        # Iterate through all numbers in the array
        for num in nums:
            # If count drops to zero, choose a new candidate
            if count == 0:
                candidate = num
            
            # Vote for the current number
            # Increment if it matches the candidate, otherwise decrement
            count += 1 if num == candidate else -1

        # By problem definition, majority element is guaranteed to exist
        return candidate
