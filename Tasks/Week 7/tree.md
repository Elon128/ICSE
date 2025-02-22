"""
Tree Theory Assignment
----------------------
This file contains answers to theoretical questions about tree structures
and implements traversal strategies for a given tree.
"""

# Answer 1: What is a tree?
# A tree is a hierarchical data structure made up of nodes.
# Each node can have a parent and multiple children.
# The top-most node is called the root, and nodes with no children are called leaf nodes.

# Answer 2: What is a leaf node?
# A leaf node is a node in the tree that does not have any children.

# Answer 3: What is a root node?
# The root node is the top-most node in the tree. It has no parent.

# Answer 4: What is the height of a tree?
# The height of a tree is the number of edges in the longest path from the root to any leaf.

# Answer 5: What is a path in a tree?
# A path in a tree is a sequence of nodes connected by edges.

# Answer 6: What are common applications of trees?
# Trees are used in:
# - File systems
# - Database indexing (e.g., B-trees)
# - Expression trees
# - Decision trees
# - Binary search trees

# Answer 7: What is a binary tree?
# A binary tree is a tree where each node can have at most two children (left and right).

# Answer 8: What is a search tree?
# A search tree is a binary tree where:
# - The left subtree of a node contains only nodes with values less than the node's value.
# - The right subtree contains only nodes with values greater than the node's value.

# Answer 9: What is a balanced search tree?
# A balanced search tree is a search tree where the height difference between the left
# and right subtrees of any node is minimized, ensuring efficient operations.

# Implementing traversal strategies for the given tree

class TreeNode:
    """Represents a single node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traversal(root):
    """Preorder Traversal: Root -> Left -> Right"""
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root):
    """Inorder Traversal: Left -> Root -> Right"""
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)


def postorder_traversal(root):
    """Postorder Traversal: Left -> Right -> Root"""
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]


def level_order_traversal(root):
    """Level Order Traversal: Level by Level"""
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


# Building the given tree
"""
      10
     / \
    /   \
   /     \
  5      15
 / \     /
2   9   13
   /   / \
  6   /   \
     12   14
"""

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(9)
root.left.right.left = TreeNode(6)
root.right.left = TreeNode(13)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(14)

# Computing traversals
preorder_result = preorder_traversal(root)
inorder_result = inorder_traversal(root)
postorder_result = postorder_traversal(root)
level_order_result = level_order_traversal(root)

# Displaying results
print("Preorder Traversal:", preorder_result)
print("Inorder Traversal:", inorder_result)
print("Postorder Traversal:", postorder_result)
print("Level Order Traversal:", level_order_result)
