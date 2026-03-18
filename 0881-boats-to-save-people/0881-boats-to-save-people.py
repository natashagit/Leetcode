class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # input: weight of people array, weight limit for each boat
        # output: minimum number of boats for pairs of people
        # sort the array
        # [1, 2, 2, 3]
        people.sort()
        start = 0
        end = len(people)-1
        boats = 0
        while start<=end:
            if people[start]+people[end]<=limit:
                start+=1
            boats+=1
            end-=1
        return boats
        

        

        