# Question 1: What is a red-black tree? Which properties does it have?

A **Red-Black Tree** is a type of self-balancing binary search tree where each node is assigned a color, either **red** or **black**.  
It maintains balance using these rules:  
1. Each node is either red or black.  
2. The root node is always black.  
3. All leaf nodes (NIL nodes) are black.  
4. A red node cannot have a red child (no two consecutive red nodes).  
5. Every path from a node to its leaf nodes has the same number of black nodes (called the black-height property). 

# Question 2: Insert the following sequence of numbers into a Red-Black Tree: [6, 7, 3, 4, 2, 1]  

**Insertions and intermediate steps:**  
**Step 1:** Insert 6 → Color root black.  
6(B)
**Step 2:** Insert 7 → 7 is red (default).  
6(B)
   \
   7(R)
**Step 3:** Insert 3 → 3 is red.  
   6(B)
  /   \
3(R)   7(R)
**Step 4:** Insert 4 → Causes red-red violation at 3-4. Perform **left rotation** at 3.  
        6(B)
       /   \
    4(R)   7(R)
    /
3(R)
**Step 5:** Insert 2 → Add as a red node under 3.  
        6(B)
        /   \
     4(B)  7(R)
     /
    3(R)
     /
     2(R)
**Step 6:** Insert 1 → Red-red violation at 2-1. Recolor 2, 4, and 6 to fix.  
Final Tree:  
       6(B)
      /   \
   4(B)   7(B)
   /       \
  3(R)     2(B)
           /
         1(R)

# Question 3: When do red-red violations occur? How does the final tree look like?  

**Red-Red Violations:**  
A red-red violation happens when a red node is added as the child of another red node.

**Final Tree:**  
       6(B)
      /   \
   4(B)   7(B)
   /       \
  3(R)     2(B)
           /
         1(R)

# Question 4: Create an AVL Tree from the same sequence of numbers: [6, 7, 3, 4, 2, 1]  
**Step-by-Step AVL Tree Insertions:**  
**Step 1:** Insert 6.  
6
**Step 2:** Insert 7.  
  6  
   \
    7
**Step 3:** Insert 3 → Balance at root (right-left rotation).  
    6
   / \
  3   7
**Step 4:** Insert 4 → No imbalance.  
    6
   / \
  3   7
   \
    4
**Step 5:** Insert 2 → Balance at 3 (right-right imbalance → rotate right).  
    6
   / \
  3   7
 /
2 4
**Step 6:** Insert 1 → Balance at 2 (right-right imbalance → rotate right).  
    6
   / \
  3   7
 /
2 4
   /
  1

**Comparison between Red-Black Tree and AVL Tree:**  
- **Red-Black Tree:** Less strictly balanced, resulting in fewer rotations.  
- **AVL Tree:** More strictly balanced, which leads to more rotations.  
- Both maintain a logarithmic height but achieve balance in different ways.

# Question 5. 2-3-4 Trees and Red-Black Trees: Corresponding Structures  

A **2-3-4 Tree** can be represented as a **Red-Black Tree**, with the following relationships:  
1. A 2-node in a 2-3-4 tree maps to a black node in a Red-Black Tree.  
2. A 3-node maps to a black node with one red child.  
3. A 4-node maps to a black node with two red children.

# Question 6. Transform the Red-Black Tree into its Corresponding 2-3-4 Tree  
From the final Red-Black Tree:  
   6(B)
  /   \
4(B)   7(B)
 / 3(R) / 2(B) / 1(R)
**Corresponding 2-3-4 Tree:**  

    [6]
   /   \
[4]     [7]
/ [2, 3, 1]

- **6** is a 2-node.  
- **4** is a 2-node.  
- **2, 3, 1** combine into a 4-node.  
This tree is equivalent to the Red-Black Tree structure.