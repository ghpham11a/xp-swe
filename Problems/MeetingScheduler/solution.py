import heapq

class Solution(object):

    def min_available_duration(self, slots1, slots2, duration):

        # Combine the slots from both people and filter out any slot that is shorter than the meeting duration.
        # This ensures we only consider slots that could potentially host the meeting.
        valid_slots = filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2)

        # Convert the filtered slots into a list.
        timeslots = list(valid_slots)

        # Convert the list into a min-heap (priority queue) based on the start time.
        # In a min-heap, the slot with the earliest start time will be at the root.
        heapq.heapify(timeslots)

        # Loop until there is fewer than 2 slots left in the heap (since we need a pair to check for an overlap).
        while len(timeslots) > 1:

            # Pop the earliest starting slot from the heap.
            _, end1 = heapq.heappop(timeslots)

            # Peek at the next earliest slot without removing it.
            # Because the heap is sorted by start time, timeslots[0] gives us the slot with the next earliest start.
            start2, _ = timeslots[0]

            # Check if the current slot (with end1) can cover a meeting starting at start2.
            # The meeting would run from start2 to start2 + duration.
            # If end1 (the end of the current slot) is at least as late as start2 + duration,
            # then there's enough overlap between the two slots for the meeting.
            if end1 >= start2 + duration:
                # Return the meeting time as soon as we find a valid overlapping period.
                return [start2, start2 + duration]
            
        # If no overlapping slot of the required duration is found, return an empty list.
        return []


solution = Solution()

assert(solution.min_available_duration(slots1=[[10,50],[60,120],[140,210]], slots2=[[0,15],[60,70]], duration=8) == [60,68])
assert(solution.min_available_duration(slots1=[[10,50],[60,120],[140,210]], slots2=[[0,15],[60,70]], duration=12) == [])

print("PASS")