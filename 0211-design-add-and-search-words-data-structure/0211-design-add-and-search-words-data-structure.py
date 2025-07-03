class TrieNode:
    def __init__(self):
        # Define structure of trie
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        # Initialize trie node
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        # For every character in word
        for c in word:
            # If not in children add new node or else move ahead
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # Set last character flag to True to mark end of word
        curr.word = True

    def search(self, word: str) -> bool:
        # Search depth wise root onwards
        def dfs(j, root):
            curr = root
            # For every character in word search
            for i in range(j, len(word)):
                c = word[i]
                # Character is "."
                if c==".":
                    # check in the children values by skipping one ahead
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)