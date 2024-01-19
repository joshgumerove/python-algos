class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie():
    def __init__(self):
        self.root = TrieNode()


new_trie = Trie()
print(new_trie.root)
