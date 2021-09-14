def eventualSafeStates(self, graph: List[List[int]]) -> List[int]:
        # 0 -> White 1 -> Grey  2 -> Black
        color = collections.defaultdict(int)
        def dfs(node):
            if color[node] != 0:
                return color[node] == 2

            color[node] = 1
            for nei in graph[node]:
                if color[nei] == 2:
                    continue
                if color[nei] == 1 or not dfs(nei):
                    return False
            color[node] = 2
            return True
        return list(filter(dfs,range(len(graph))))
