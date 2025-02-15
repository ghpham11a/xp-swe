from collections import defaultdict

class Solution:
    
    def critical_connections(self, n, connections):

        # Build Graph and Edge Map
        graph = defaultdict(list)
        unique_edges = set()
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)

            unique_edges.add((min(src, dst), max(src, dst)))

        # Initialize low_links
        low_links = [None for i in range(n)]

        self.dfs(graph, low_links, unique_edges, 0, 0)
        
        # format result
        result = []
        for u, v in unique_edges:
            result.append([u, v])
        
        return result
            
    def dfs(self, graph, low_links, unique_edges, node, time):
        
        # That means this node is already visited. We simply return the rank.
        if low_links[node]:
            return low_links[node]
        
        # Update the rank of this node.
        low_links[node] = time
        
        # This is the max we have seen till now. So we start with this instead of INT_MAX or something.
        min_time = time + 1
        for neighbor in graph[node]:
            
            # Skip the parent.
            if low_links[neighbor] and low_links[neighbor] == time - 1:
                continue
                
            # Recurse on the neighbor.    
            recursive_rank = self.dfs(graph, low_links, unique_edges, neighbor, time + 1)
            
            # Step 1, check if this edge needs to be discarded.
            if recursive_rank <= time:
                unique_edges.remove((min(node, neighbor), max(node, neighbor)))
            
            # Step 2, update the minRank if needed.
            min_time = min(min_time, recursive_rank)
        
        return min_time

runner = Solution()

assert(runner.critical_connections(4, [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]])

print("PASS")