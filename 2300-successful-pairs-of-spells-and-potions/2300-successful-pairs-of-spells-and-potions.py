class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # input: spells and potions arrays, success value
        # output: 
        # return array pairs where pairs[i] = count of pairs that satisfy the condition:
        # spells[i]*potions>=success value

        # O(n*m)
        # pairs = [0]*len(spells)
        # for i in range(len(spells)):
        #     count = 0
        #     for j in range(len(potions)):
        #         if spells[i]*potions[j]>=success:
        #             count+=1
        #     pairs[i] = count
        # return pairs
        potions.sort()
        pairs = [0]*len(spells)
        def binary_search(a):
            low = 0
            high = len(potions)-1
            while low<high:
                mid = (low+high)//2
                if potions[mid]*a>=success:
                    high = mid
                else:
                    low = mid+1
            return high if potions[high]*a>=success else -1
            #index from where success begins

        for i in range(len(spells)):
            pivot = binary_search(spells[i])
            if pivot==-1:
                pairs[i]=0
            else:
                pairs[i]=len(potions)-pivot
        return pairs