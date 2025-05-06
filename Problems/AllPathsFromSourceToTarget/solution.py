class Solution:

    # Main function to find all paths from node 0 to node n - 1
    def all_paths_source_target(self, graph):
        target = len(graph) - 1  # The destination node (last node in the graph)
        output = []              # List to store all valid paths
        sub_output = [0]         # Current path being built, starting from node 0

        # Start backtracking from node 0
        self.backtrack(graph, target, output, 0, sub_output)

        return output            # Return all the valid paths

    # Helper function to perform backtracking
    def backtrack(self, graph, target, output, src, sub_output):

        # If the current node is the target, store a copy of the current path
        if src == target:
            output.append(list(sub_output))  # Make a copy of sub_output
            return

        # Explore all neighbors of the current node
        for dst in graph[src]:
            sub_output.append(dst)                          # Add the neighbor to the path
            self.backtrack(graph, target, output, dst, sub_output)  # Recurse with the new node
            sub_output.pop()                                # Backtrack by removing the last node