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
        dict_s = {}
        for s in strs:
            if ''.join(sorted(s)) in dict_s:
                dict_s[''.join(sorted(s))].append(s)
            else:
                dict_s[''.join(sorted(s))] = [s]
        return list(dict_s.values())