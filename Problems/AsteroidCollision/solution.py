class Solution:
    def asteroid_collision(self, asteroids):
        
        stack = []

        for a in asteroids:
            # Handle possible collisions
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    # Right-moving one is smaller and explodes
                    stack.pop() 
                    continue
                elif stack[-1] == -a:
                    # Both explode
                    stack.pop()
                break
            else:
                stack.append(a)

        return stack