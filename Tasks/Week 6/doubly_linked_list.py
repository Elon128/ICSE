class DoublyLinkedNode:
    """
    Represents a single node in the doubly linked list.
    Each node contains a value, a reference to the previous node, and a reference to the next node.
    """
    def __init__(self, value=None, prev=None, next=None):
        self.value = value  # The value of the node (None for dummy nodes)
        self.prev = prev    # Reference to the previous node
        self.next = next    # Reference to the next node


class DoublyLinkedList:
    """
    A doubly linked list with dummy head and tail nodes.
    Supports common operations like adding, removing, and accessing nodes.
    """
    def __init__(self):
        # Initialize the dummy head and tail nodes
        self._head = DoublyLinkedNode()  # Dummy head node
        self._tail = DoublyLinkedNode()  # Dummy tail node

        # Link head to tail and tail to head
        self._head.next = self._tail
        self._tail.prev = self._head

        # Keep track of the number of real nodes in the list
        self._size = 0

    def __len__(self) -> int:
        """
        Returns the number of items in the list.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        Returns True if there are no real nodes, False otherwise.
        """
        return self._size == 0

    def add_first(self, item: int) -> None:
        """
        Adds a new node with the given item to the front of the list.
        Steps:
        1. Create a new node.
        2. Insert it between the head and the first real node.
        3. Update pointers and increase size.
        """
        new_node = DoublyLinkedNode(item, self._head, self._head.next)
        self._head.next.prev = new_node
        self._head.next = new_node
        self._size += 1

    def get_first(self) -> int | None:
        """
        Returns the value of the first real node in the list.
        If the list is empty, returns None.
        """
        return None if self.is_empty() else self._head.next.value

    def remove_first(self) -> int | None:
        """
        Removes the first real node in the list and returns its value.
        Steps:
        1. Check if the list is empty. If yes, return None.
        2. Unlink the first real node.
        3. Update pointers and decrease size.
        """
        if self.is_empty():
            return None
        first_node = self._head.next
        self._head.next = first_node.next
        first_node.next.prev = self._head
        self._size -= 1
        return first_node.value

    def add_last(self, item: int) -> None:
        """
        Adds a new node with the given item to the end of the list.
        Steps:
        1. Create a new node.
        2. Insert it between the tail and the last real node.
        3. Update pointers and increase size.
        """
        new_node = DoublyLinkedNode(item, self._tail.prev, self._tail)
        self._tail.prev.next = new_node
        self._tail.prev = new_node
        self._size += 1

    def get_last(self) -> int | None:
        """
        Returns the value of the last real node in the list.
        If the list is empty, returns None.
        """
        return None if self.is_empty() else self._tail.prev.value

    def remove_last(self) -> int | None:
        """
        Removes the last real node in the list and returns its value.
        Steps:
        1. Check if the list is empty. If yes, return None.
        2. Unlink the last real node.
        3. Update pointers and decrease size.
        """
        if self.is_empty():
            return None
        last_node = self._tail.prev
        self._tail.prev = last_node.prev
        last_node.prev.next = self._tail
        self._size -= 1
        return last_node.value

    def at(self, i: int) -> int:
        """
        Returns the value at the ith node (0-indexed).
        Steps:
        1. Check if the index is valid. Raise an error if out of bounds.
        2. Traverse the list to the ith node.
        3. Return the value of the node.
        """
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        current = self._head.next
        for _ in range(i):
            current = current.next
        return current.value

    def __str__(self) -> str:
        """
        Returns a string representation of the list, showing the values of all nodes.
        Example: "10 <-> 20 <-> 30"
        """
        items = []
        current = self._head.next
        while current != self._tail:
            items.append(str(current.value))
            current = current.next
        return " <-> ".join(items)


# Testing the DoublyLinkedList
if __name__ == "__main__":
    dll = DoublyLinkedList()
    print("Is the list empty?", dll.is_empty())  # True

    # Add items to the front
    dll.add_first(10)
    dll.add_first(20)
    dll.add_first(30)
    print("List after adding items to the front:", dll)  # "30 <-> 20 <-> 10"

    # Add items to the end
    dll.add_last(40)
    dll.add_last(50)
    print("List after adding items to the end:", dll)  # "30 <-> 20 <-> 10 <-> 40 <-> 50"

    # Get first and last items
    print("First item:", dll.get_first())  # 30
    print("Last item:", dll.get_last())  # 50

    # Remove first and last items
    print("Removed first item:", dll.remove_first())  # 30
    print("Removed last item:", dll.remove_last())  # 50
    print("List after removals:", dll)  # "20 <-> 10 <-> 40"

    # Get item at a specific position
    print("Item at index 1:", dll.at(1))  # 10

    # Length of the list
    print("Length of the list:", len(dll))  # 3
