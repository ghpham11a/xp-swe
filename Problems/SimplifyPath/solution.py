class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Stack to keep track of valid directory names
        cur = ""    # Current directory name being processed

        # Add an extra "/" to process the last directory/file without extra logic
        for c in path + "/":
            if c == "/":
                # Encountering a slash means we finished reading one part (directory name)

                if cur == "..":
                    # ".." means move up to the parent directory (pop if possible)
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    # A valid directory name (non-empty and not ".") gets added to the stack
                    stack.append(cur)
                # Reset cur to start reading the next part
                cur = ""
            else:
                # If not a slash, accumulate characters into the current directory name
                cur += c

        # Join the stack with slashes to form the simplified canonical path
        return "/" + "/".join(stack)