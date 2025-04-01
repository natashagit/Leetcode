class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                # Creating new reference node for new alphabet
                current_node.children[char] = TrieNode()
            # Since already alphabet is present, go to next reference children
            current_node = current_node.children[char]
        # End the word after all alphabets inserted
        current_node.endOfWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # start with root
        current_node = self.root
        # Loop through all alphabets in the word
        for char in word:
            # Check if alphabet is present in trie
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # returns true if whole word present 
        return current_node.endOfWord
        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for char in prefix:
            # Check if alphabet is present in trie
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Returns true if prefix present in trie
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)