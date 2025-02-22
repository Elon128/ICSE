# Question 1: What is a 2 - 3 - 4 tree?
Solution: A **2-3-4 Tree** is a type of balanced search tree characterized by the following properties:
1. Each internal node can have 2, 3, or 4 children.
2. A node with (d) children will contain (d - 1) keys.
3. The keys within each node are arranged in sorted order, ensuring the search tree property is upheld.

### Types of Nodes:

# 1. 2-Node:
#    - 1 key, 2 children.
       12
      /  \
    10    15

# 2. 3-Node:
#    - 2 keys, 3 children.
       12 | 17
      /   |   \
    10    15    18

# 3. 4-Node:
#    - 3 keys, 4 children.
    12 | 17 | 23
   /    |    |    \
  10    15   18    25

### Key Points:
- A 2-node has one key and splits into two subtrees.
- A 3-node has two keys and splits into three subtrees.
- A 4-node has three keys and splits into four subtrees.
- The tree remains balanced because all leaves are at the same level.

This structure ensures efficient searching, insertion, and deletion operations.

# Question 2: The order in which we insert nodes into a 2 - 3 -4 tree is important for the final structure of the tree. Show that with the following example:
# 1. Insert the numbers 3, 7, 5, 15, 17, 9, 13, 21, 11, 19 into a 2 - 3 - 4 tree.
# 2. Do the same but in different order 3, 5, 7, 9, 11, 13, 15, 17, 19, 21!
# 3. What difference do you see?
Solution: 
# Effect of Insertion Order on a 2-3-4 Tree

### Example 1: Inserting 3, 7, 5, 15, 17, 9, 13, 21, 11, 19

**Step 1:** Insert 3, 7, 5  
    3 | 5 | 7  

**Step 2:** Insert 15, 17 → Split 4-node (3 | 5 | 7)  
        5  
      /   \  
    3     7 | 15 | 17  

**Step 3:** Insert 9 → Add to 7-node  
        5  
      /   \  
    3     7 | 9 | 15 | 17   

**Step 4:** Insert 13, 21 → Split again at 7-node  
        9  
      /   |     \  
    5    7 | 13  15 | 17 | 21  

**Step 5:** Insert 11 → Add to 7-node  
        9  
      /   |     \  
    5    7 | 11 | 13   15 | 17 | 21  

---

### Example 2: Inserting 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 (Sorted Order)

**Step 1:** Insert 3, 5, 7 → Form a 4-node  
    3 | 5 | 7  

**Step 2:** Insert 9 → Split 4-node  
        5  
      /   \  
    3     7 | 9  

**Step 3:** Insert 11, 13 → Add to 7-node  
        5  
      /   \  
    3     7 | 9 | 11 | 13  

**Step 4:** Insert 15 → Split 4-node  
        9  
      /   |     \  
    5    7      11 | 13 | 15  

**Step 5:** Insert 17, 19, 21 → Continue adding  
        9  
      /   |     \  
    5    7      11 | 13 | 15 | 17 | 19 | 21  

---

### Observations:

1. First Order (Unsorted):  
   - Splits happen at various points because items are added in random order.  
   - The tree ends up balanced, but splits occur sooner during the process.  

2. Second Order (Sorted):  
   - Splits are more predictable as nodes fill up one after the other.  
   - The tree grows more steadily with fewer early splits.

The order of insertion affects when and where splits occur, impacting the final structure of the 2-3-4 tree.  

# Question 3: During the lecture we discussed two different strategies of building 2-3-4 trees: bottom-up and top-down. What are the main differences between the two approaches?
# which method did you use for the second subtask? Would the resulting tree look any different in the end?
Solution:
### Bottom-Up vs. Top-Down Approach

1. Bottom-Up Approach:  
   - Nodes are split after they become full while working back up the tree.  
   - Splits occur as you return upward during the insertion process.  

2. Top-Down Approach:**  
   - Nodes are split before moving into full nodes during insertion.  
   - Splits happen on the way down to make room for new keys.

### Method Used for Second Subtask  
We used the Bottom-Up approach, as splits occurred after filling nodes while moving back up the tree.

### Final Tree Structure  
The resulting tree would look the same in both approaches because a 2-3-4 tree ensures balance regardless of the strategy.  
The only difference is when splits occur during insertion.



