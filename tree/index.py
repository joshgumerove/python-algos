class TreeNode():
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


# create root first
tree = TreeNode('Drinks', [])

print(tree)

cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])

tree.addChild(cold)
tree.addChild(hot)

print(tree)
print("*********")

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])

hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fanta)

print(tree)


# used to represent data in heirarchical form
# like a reverse tree in real life
# more specialized as go down the tree
# every node has two components (data and reference to its subcategory)
# tree is a nonlinear data structure
