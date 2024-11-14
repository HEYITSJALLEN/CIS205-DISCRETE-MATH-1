class TreeNode:
    def human(self, value):
        self.value = value  # Node value
        self.children = []  # List of children (subtrees)

    def add_child(self, child):
        self.children.append(child)

def preorder(node):
    if node is None:
        return
    
    # Write the node value (print it for this example)
    print(node.value)
    
    # Recursively traverse each child in the tree
    for child in node.children:
        preorder(child)

# Example usage:
# Create nodes
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

# Build tree structure
root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)

# Call preorder traversal
preorder(root)
