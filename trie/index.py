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

    def search_for_string(self, word):
        current_node = self.root

        for i in word:
            node = current_node.children.get(i)
            if node == None:
                return False
            current_node = node
        if current_node.end_of_string == True:
            return True
        else:
            return False


new_trie = Trie()
new_trie.insert_string("App")
new_trie.insert_string("Appl")

print("***search_for_string***")
print(new_trie.search_for_string("App"))
print(new_trie.search_for_string("Ap"))
print(new_trie.search_for_string("DCD"))
