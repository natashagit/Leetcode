class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            #directed edge in adj list
            adj[course].append(pre)
        
        # courses visiting
        visited = [False]*numCourses
        # detect cycle
        onepath = [False]*numCourses

        def dfs(course):
            # if course already true- visited - loop detected
            if onepath[course]:
                return False
            # course can be completed if it does not have prereqs
            if visited[course]:
                return True
            # Mark as detected
            onepath[course] = True

            # Loop through all prereqs
            for pre in adj[course]:
                if not dfs(pre):
                    return False

            # Mark as visited
            visited[course] = True
            # Reset to false
            onepath[course] = False
            return True

        # Running dfs on courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

