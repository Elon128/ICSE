class BinaryTree:
    def __init__(self, data: int, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent  # Add a parent pointer for traversal convenience

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def height(self):
        """Calculate the height of the subtree rooted at this node."""
        if self is None:
            return 0
        left_height = self.get_left().height() if self.get_left() else 0
        right_height = self.get_right().height() if self.get_right() else 0
        return 1 + max(left_height, right_height)

    def is_balanced(self) -> bool:
        """Check whether the subtree rooted at this node is AVL balanced."""
        if self is None:
            return True

        left_height = self.get_left().height() if self.get_left() else 0
        right_height = self.get_right().height() if self.get_right() else 0

        if abs(left_height - right_height) > 1:
            return False

        left_balanced = self.get_left().is_balanced() if self.get_left() else True
        right_balanced = self.get_right().is_balanced() if self.get_right() else True

        return left_balanced and right_balanced

    def inorder_next(self) -> "BinaryTree" | None:
        """
        Find the inorder successor of this node in a binary search tree.
        Return None if no such successor exists.
        """
        if self.get_right():
            # The next node is the leftmost node of the right subtree
            current = self.get_right()
            while current.get_left():
                current = current.get_left()
            return current

        # If no right subtree, go up the tree to find the next higher parent
        current = self
        parent = self.get_parent()
        while parent and current == parent.get_right():
            current = parent
            parent = parent.get_parent()

        return parent

    def add_left(self, value):
        """Add a left child."""
        self.left = BinaryTree(value, parent=self)

    def add_right(self, value):
        """Add a right child."""
        self.right = BinaryTree(value, parent=self)