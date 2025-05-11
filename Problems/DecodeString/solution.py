class Solution:
    
    def decode_string(self, s):
        # Stack to keep track of characters, numbers, and intermediate results
        stack = []

        # Traverse each character in the input string
        for i in range(len(s)):
            if s[i] != "]":
                # If current character is not a closing bracket, push to stack
                # This includes digits, letters, and opening brackets
                stack.append(s[i])
            else:
                # When we find a closing bracket, start decoding

                # Step 1: Extract the encoded string inside the brackets
                sub_str = ""
                while stack[-1] != "[":
                    # Pop characters and build the substring in reverse
                    sub_str = stack.pop() + sub_str
                stack.pop()  # Discard the opening bracket '['

                # Step 2: Extract the multiplier (number k)
                k = ""
                while stack and stack[-1].isdigit():
                    # Pop digits and build the number (could be multi-digit)
                    k = stack.pop() + k

                # Step 3: Repeat the substring k times and push back to stack
                stack.append(int(k) * sub_str)

        # Join everything in the stack to form the final result string
        return "".join(stack)