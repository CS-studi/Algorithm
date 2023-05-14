class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for pr in prerequisites:
            a, b = pr
            graph[a].append(b)

        def dfs(node):
            if visited[node] == 1:  # 불완전한 방문을 한 경우라면 -> 사이클이 일어난거임
                return False

            if visited[node] == -1:  # 갓벽한 방문을 했던 경우
                return True

            visited[node] = 1  # 방문 시작
            for pre_node in graph[node]:
                if visited[pre_node] == 1:
                    return False
                if not dfs(pre_node):
                    return False
            visited[node] = -1  # 완벽한 방문

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
