class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter

        freq_dict = Counter(words)
        
        import heapq
        max_heap = [(-freq, word) for word, freq in freq_dict.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]

        
    

