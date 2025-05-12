class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])  # Get number of rows (R) and columns (C)
        color = image[sr][sc]  # Store the original color at the starting pixel

        # If the new color is the same as the original color, there's nothing to change
        if color == newColor:
            return image

        # Define the recursive DFS function
        def dfs(r, c):
            # If the current pixel has the original color, update it
            if image[r][c] == color:
                image[r][c] = newColor  # Change the color

                # Explore the pixel above if within bounds
                if r >= 1:
                    dfs(r - 1, c)
                # Explore the pixel below if within bounds
                if r + 1 < R:
                    dfs(r + 1, c)
                # Explore the pixel to the left if within bounds
                if c >= 1:
                    dfs(r, c - 1)
                # Explore the pixel to the right if within bounds
                if c + 1 < C:
                    dfs(r, c + 1)

        # Start the flood fill from the given starting pixel
        dfs(sr, sc)

        return image  # Return the modified image