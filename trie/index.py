class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_of_string = True
        print("Successfully inserted")


new_trie = Trie()
new_trie.insert_string("App")
new_trie.insert_string("Appl")
