from binary_tree import BinaryTree


class MyBinaryTree(BinaryTree):
    """
    Extends the BinaryTree class to handle integer elements and implements
    additional methods for height, max sum, max path, and max width.
    """

    def height(self) -> int:
        """
        Calculates the height of the tree starting from this node.

        Returns:
            int: The height of the tree.
        """
        if self is None:
            return -1
        left_height = self.get_left().height() if self.get_left() else 0
        right_height = self.get_right().height() if self.get_right() else 0
        return 1 + max(left_height, right_height)

    def max_sum(self) -> int:
        """
        Calculates the sum of the subtree starting from this node, including all its children.

        Returns:
            int: The total cumulative sum of the subtree rooted at this node.
        """
        if self is None:
            return 0

        left_sum = self.get_left().max_sum() if self.get_left() else 0
        right_sum = self.get_right().max_sum() if self.get_right() else 0

        return self.get_item() + left_sum + right_sum

    def max_path(self) -> int:
        """
        Finds the maximal path sum starting from this node to any leaf.

        Returns:
            int: The maximum path sum.
        """
        if self is None:
            return 0
        left_path = self.get_left().max_path() if self.get_left() else 0
        right_path = self.get_right().max_path() if self.get_right() else 0
        return self.get_item() + max(left_path, right_path)

    def max_width(self) -> int:
        """
        Calculates the maximum width of the tree (i.e., the maximum number
        of nodes at any level).

        Returns:
            int: The maximum width of the tree.
        """
        if self is None:
            return 0
        queue = [self]
        max_width = 0
        while queue:
            level_width = len(queue)
            max_width = max(max_width, level_width)
            for _ in range(level_width):
                node = queue.pop(0)
                if node.get_left():
                    queue.append(node.get_left())
                if node.get_right():
                    queue.append(node.get_right())
        return max_width


if __name__ == "__main__":
    # Example tree for testing
    root = MyBinaryTree(1)
    root.set_left(MyBinaryTree(2))
    root.set_right(MyBinaryTree(3))
    root.get_left().set_left(MyBinaryTree(4))
    root.get_left().set_right(MyBinaryTree(5))
    root.get_right().set_right(MyBinaryTree(6))
    root.get_right().get_right().set_left(MyBinaryTree(7))

    # Test height
    print("Height of the tree:", root.height())

    # Test max sum
    print("Maximum sum of child subtrees:", root.max_sum())

    # Test max path
    print("Maximum path sum:", root.max_path())

    # Test max width
    print("Maximum width of the tree:", root.max_width())
