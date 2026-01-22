class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # input: beginword, endword, list of words
        # output: length of shortest sequence following the instructions
        # each word is a node, an edge exists if they have only one different letter
        # shortest path in the graph-bfs
        from collections import deque
        q = deque()
        # keep count for path length
        q.append((beginWord,1))
        wordSet = set(wordList)
        
        visited = set(beginWord)
        while q:
            word, level = q.popleft()
            if word==endWord:
                return level
            for i in range(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i]+j+word[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word,level+1))
        
        return 0


