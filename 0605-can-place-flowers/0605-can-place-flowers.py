class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        # Understand
        # inputs: list of potted plants, number of 1's to be inserted
        # outputs: True/False
        # constraints: Can't plant in adjacent plots
        # edge cases: empty list

        # Plan
        # move pointer through flowerbed
        i=0
        if len(flowerbed)==1:
            return (flowerbed[0] == 0 and n <= 1) or n == 0

        while i < len(flowerbed) and n>0:
            # Search for 0's
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                # if first element 0, check right element is 0
                        # then decrement n, as its planted now
                        n-=1
                        flowerbed[i]=1
                        # move the pointer two steps ahead
                        i+=2
                        continue
                else:
                    i+=1
            elif i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    n-=1
                    flowerbed[i]=1
                break      
            else:
                if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                        # if the left and right element of that 0 is 0
                        # then decrement n, as its planted now
                        n-=1
                        flowerbed[i]=1
                        # move the pointer to two steps ahead
                        i+=2
                        
                else:
                    i+=1
        if n==0:
            return True
        else:
            return False
