class Solution:

    def car_fleet(self, target, position, speed):
        # Pair up each car's position and speed
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []  # This will hold the "arrival time" of each fleet

        # Sort cars by starting position in descending order (farthest from target first)
        for p, s in sorted(pair)[::-1]:
            # Calculate time it takes for the car to reach the target
            time = (target - p) / s
            stack.append(time)

            # If the current car arrives **no later** than the one in front,
            # it merges into the same fleet (pop current one)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Merge into the fleet ahead

        # The remaining items in the stack represent separate fleets
        return len(stack)
    
solution = Solution()

assert(solution.car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3)

print("PASS")