class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # input: edges
        # output: edge that has to be removed so that tree is formed
        # while adding edges to graph, check if there is already a path existing between those points
        # if so then return

        graph = defaultdict(list)
        # fn to check if path exists
        def dfs(src, target, visited):
            # base case
            if src == target:
                return True
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

        for u,v in edges:
            visited = set()
            # checking if there is already a path btwn u and v
            if dfs(u,v,visited):
                return [u,v]
            # since no path, add edge to the graph
            graph[u].append(v)
            graph[v].append(u)

