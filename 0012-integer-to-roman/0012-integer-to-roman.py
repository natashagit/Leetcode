class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # input: number
        # output: roman integer
        # list of values with symbol in descending order
        # can loop through it and keep dividing the number with the value and checking the symbol to place 
        map_nums = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

        result = ""
        for val, sym in map_nums:
            count = num//val
            if count>0:
                result+=(sym*count)
                num = num%val
        return result

