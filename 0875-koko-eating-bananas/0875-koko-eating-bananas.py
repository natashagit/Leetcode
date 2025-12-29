class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # input: list of bananas in each pile, h hours to eat 
        # output: eating speed such that all bananas can be finished within h 

        # 1 <= k <= max(piles)
        # total time += ceil(piles[i]/k)

        # make a function to calculate total time for each k
            # total time = sum(pile[i]/k)
        # do binary search to find the best k that gives total time<=h
        
        import math
        def fn_total(arr, k):
            i = 0
            total_time = 0
            while i<len(arr):
                total_time+=math.ceil(arr[i]/float(k))
                i+=1
            return total_time

        result = max(piles)
        low = 1
        high = max(piles)
        while low<=high:
            mid = (low+high)//2
            total_time = fn_total(piles, mid)
            if total_time<=h:
                result = mid
                high = mid-1
            else:
                low=mid+1
        return result

            

        

        
    
        
        