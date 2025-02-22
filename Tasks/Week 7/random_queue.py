from typing import Any, Optional
import random

from icse_queue import Queue


class RandomQueue(Queue):
    """
    A queue that supports random removal and sampling of elements.
    """

    def __init__(self):
        """
        Initializes the RandomQueue with an empty list to store items.
        """
        self._items = []

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue has no elements, False otherwise.
        """
        return len(self._items) == 0

    def enqueue(self, item: Any) -> bool:
        """
        Adds `item` to the queue.

        Args:
            item (Any): The item to add.

        Returns:
            bool: True to indicate the item was added successfully.
        """
        self._items.append(item)
        return True

    def dequeue(self) -> Optional[Any]:
        """
        Removes and returns one random item from the queue (sampling without replacement).

        Returns:
            Optional[Any]: The removed item, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        random_index = random.randint(0, len(self._items) - 1)
        return self._items.pop(random_index)

    def sample(self) -> Optional[Any]:
        """
        Returns one random item from the queue without removing it.

        Returns:
            Optional[Any]: A random item, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        random_index = random.randint(0, len(self._items) - 1)
        return self._items[random_index]


if __name__ == "__main__":
    rq = RandomQueue()

    print("Is the queue empty?", rq.is_empty())  # True

    # Add items to the queue
    rq.enqueue("apple")
    rq.enqueue("banana")
    rq.enqueue("cherry")
    print("Is the queue empty?", rq.is_empty())  # False

    # Sample random items
    print("Sampled item:", rq.sample())  # Randomly returns one of
