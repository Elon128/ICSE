# Question 1: Explain what and AVL tree is! Why is it necessary to balance trees?
Solution: An AVL tree is a binary search tree that maintains balance by ensuring the height difference between the left and right subtrees (balance factor) of every node is either -1, 0, or +1. This self-balancing mechanism keeps the tree’s height at \(O(\log n)\), ensuring efficient performance. Without this balance, the tree can become skewed into a linear structure, similar to a linked list, which significantly slows down search, insertion, and deletion operations.

# Question 2: Explain the algorithm for inserting node into an AVL tree using the sequence 14, 17, 19, 7, 5, 10, 18
Solution: Inserting Nodes into an AVL Tree (Sequence: 14, 17, 19, 7, 5, 10, 18)

1. Insert the Node: Add the node to the tree as you would in a standard Binary Search Tree (BST).
2. Update Heights: Adjust the height of the current node after insertion.
3. Check Balance Factor: Calculate the balance factor using the formula:
   Balance Factor = Height(Left Subtree) - Height(Right Subtree)
   If the balance factor is outside the range [-1, 0, 1], the tree becomes unbalanced.
4. Rebalance the Tree: Apply the appropriate rotation(s) based on the imbalance type:
   - LL Imbalance (Left-Left): Perform a single Right Rotation.
   - RR Imbalance (Right-Right): Perform a single Left Rotation.
   - LR Imbalance (Left-Right): Perform a Left Rotation on the left child, followed by a Right Rotation.
   - RL Imbalance (Right-Left): Perform a Right Rotation** on the right child, followed by a Left Rotation.

# Question 3: Show how the tree looks like after every important step.
Solution:  
# Step 1: Insert 14  
    14  
    Tree is balanced  

# Step 2: Insert 17  
    14  
      \  
       17  
    Tree is balanced  

# Step 3: Insert 19  
    14  
      \  
       17  
         \  
          19  
    In this step, there is a Right-Right (RR) imbalance at 14.  
    Perform **Left Rotation**.  

    Resulting Tree:  
        17  
       /  \  
      14   19  
    Tree is balanced  

# Step 4: Insert 7  
        17  
       /  \  
      14   19  
     /  
    7  
    Tree is balanced  

# Step 5: Insert 5  
        17  
       /  \  
      14   19  
     /  
    7  
   /  
  5  
    In this step, there is a Left-Left (LL) imbalance at 14.  
    Perform **Right Rotation**.  

    Resulting Tree:  
        17  
       /  \  
      7    19  
     / \  
    5   14  
    Tree is balanced  

# Step 6: Insert 10  
        17  
       /  \  
      7    19  
     / \  
    5   14  
       /  
      10  
    In this step, there is a Left-Right (LR) imbalance at 7.  
    Perform **Left Rotation** on 14, then **Right Rotation** on 7.  

    Resulting Tree:  
        17  
       /  \  
      10   19  
     /  \  
    7    14  
   /  
  5  
    Tree is balanced  

# Step 7: Insert 18  
        17  
       /  \  
      10   19  
     /  \  /  
    7   14 18  
   /  
  5  
    Tree is balanced  

# Final Tree:  
        17  
       /  \  
      10   19  
     /  \  /  
    7   14 18  
   /  
  5  

   
