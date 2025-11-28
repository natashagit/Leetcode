class Solution(object):
    # input: array of strings strs
    # output: list of lists having similar anagrams together
    # loop through the list of strs
    # have a dict to store the key as sorted(str) with the values as the str
    # keep checking if sorted(str) already present in the dict, then just append the str to the values
    # return the list of all the values
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_strs = {}
        for i in strs:
            if ''.join(sorted(i)) in dict_strs:
                dict_strs[''.join(sorted(i))].append(i)
            else:
                dict_strs[''.join(sorted(i))]=[i]
        return list(dict_strs.values())


        