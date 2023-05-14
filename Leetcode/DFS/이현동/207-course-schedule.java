class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        degree = [0 for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1
        
        zeroDegreeLst = [i for i in range(numCourses) if degree[i] == 0]
        
        for i in zeroDegreeLst:
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    zeroDegreeLst.append(j)
        
        return len(zeroDegreeLst) == numCourses
            
        
                
            
        