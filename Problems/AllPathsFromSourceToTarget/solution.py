class Solution:

    def all_paths_source_target(self, graph):
        target = len(graph) - 1
        output = []
        sub_output = [0]
        self.backtrack(graph, target, output, 0, sub_output)

        return output

    def backtrack(self, graph, target, output, src, sub_output):

        if src == target:
            output.append(list(sub_output))
            return

        for dst in graph[src]:
            sub_output.append(dst)
            self.backtrack(graph, target, output, dst, sub_output)
            sub_output.pop()