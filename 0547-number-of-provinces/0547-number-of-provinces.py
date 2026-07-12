class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        # [[1,1,0],
        # [1,1,0],
        # [0,0,1]]
        visited = set()
        from collections import deque
        
        rows, cols = len(isConnected), len(isConnected)
        provinces = 0
        q = deque()
        for city in range(rows):
            if city in visited:
                continue

            provinces+=1
            
            q.append(city)
            visited.add(city)

            while q:
                current_city = q.popleft()

                for neighbor in range(cols):
                    if isConnected[current_city][neighbor]==1 and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        return provinces   






                    
