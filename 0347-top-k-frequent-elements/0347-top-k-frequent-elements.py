class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map_dict = {}
        for num in nums:
            if num in map_dict:
                map_dict[num]+=1
            else:
                map_dict[num]=1
        freq=[[] for i in range(len(nums)+1)]

        for number, count in map_dict.items():
            freq[count].append(number)
        
        result=[]
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result
