import collections

class Solution(object):
    def max_sliding_window(self, nums, k):
        # Initialize a deque (double-ended queue) to store indices of the elements.
        # This deque will maintain indices in such a way that the values they point to are in 
        # decreasing order from the front (largest) to the back (smallest). 
        deque = collections.deque()
        
        # This list will collect the maximum value for each sliding window.
        output = []
        
        # Process the first window of size k.
        # For each index in the first k elements:
        for index in range(k):
            # While the deque is not empty and the current element is greater than or equal to 
            # the element corresponding to the index at the back of the deque,
            # remove that index since it can never be the maximum if nums[index] is larger.
            while deque and nums[index] >= nums[deque[-1]]:
                deque.pop()
            # Append the current index to the deque.
            deque.append(index)
        
        # The element at the front of the deque is the largest element for the first window.
        output.append(nums[deque[0]])
        
        # Process the rest of the elements (each representing the new element in the sliding window).
        for index in range(k, len(nums)):
            # Remove the index at the front of the deque if it is out of the current window's bound.
            # The current window's starting index is index - k.
            if deque and deque[0] == index - k:
                deque.popleft()
            
            # Remove indices from the back if their corresponding values are less than or equal to 
            # the current element (nums[index]). They are no longer needed as they cannot contribute 
            # to a maximum if the current element is larger.
            while deque and nums[index] >= nums[deque[-1]]:
                deque.pop()
            
            # Add the current index to the deque.
            deque.append(index)
            
            # The current maximum is at the front of the deque, so add it to the output list.
            output.append(nums[deque[0]])
        
        # Return the list of maximums for each sliding window.
        return output
            
solution = Solution()

assert(solution.max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])

print("PASS")