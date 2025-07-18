class Solution:
    def climbStairs(self, n: int) -> int:
        # Tabulation
        one = two = 1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one
        
        # if n==0:
        #     return 1
        # if n==1:
        #     return 1
        # one = self.climbStairs(n-1)
        # two = self.climbStairs(n-2)
        # return one+two