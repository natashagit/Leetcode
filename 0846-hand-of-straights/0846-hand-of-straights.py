class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        from collections import Counter
        count = Counter(hand)
        hand.sort()
        if len(hand)%groupSize!=0:
            return False

        # [1,2,2,3,3,4,6,7,8]
        
        for num in hand:
            if count[num]:
                for i in range(num, num+groupSize):
                    if count[i]==0:
                        return False
                    count[i]-=1
        return True