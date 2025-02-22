
# Graph Analysis Assignment

---

### **1. What is a graph?**
A **graph** is a way to represent relationships or connections between things. It consists of:
- **Vertices (or nodes)**: These represent entities, like people, cities, or objects.
- **Edges (or connections)**: These represent relationships between the nodes, like roads between cities or friendships in a social network.

---

### **2. What is a directed and undirected graph? What is this graph?**
- A **directed graph** has edges with direction, like one-way streets. The direction is shown with arrows.
- An **undirected graph** has edges without direction, meaning the connection works both ways, like two-way streets.

**This graph** is a **directed graph** because the edges have arrows indicating direction.

---

### **3. How many vertices does this graph have?**
This graph has **8 vertices**. These are labeled as `1, 2, 3, 4, 5, 6, 7, and 8`.

---

### **4. How many edges does this graph have?**
This graph has **13 edges**, as shown by the arrows connecting the nodes.

---

### **5. List all sources.**
A **source** is a node that only has outgoing edges (no incoming edges).  
In this graph:
- **Source**: Node `1`.

---

### **6. List all sinks.**
A **sink** is a node that only has incoming edges (no outgoing edges).  
In this graph:
- **Sink**: Node `3`.

---

### **7. How many cycles of length 2 and 3 are in this graph?**
A **cycle** is a path that starts and ends at the same node.

- **Cycles of length 2**:
  - Node `6` loops to itself: `(6 -> 6)`.
  - Node `8` loops to itself: `(8 -> 8)`.

- **Cycles of length 3**:
  - `(6 -> 0 -> 5 -> 6)` forms a cycle.

---

### **8. What is the edge list for this graph?**
The **edge list** shows all connections as pairs (`from`, `to`).  
For this graph:
1. `1 -> 2`
2. `1 -> 5`
3. `2 -> 3`
4. `3 -> 4`
5. `4 -> 1`
6. `5 -> 6`
7. `5 -> 0`
8. `6 -> 6` (self-loop)
9. `6 -> 7`
10. `7 -> 0`
11. `0 -> 8`
12. `8 -> 8` (self-loop)

---

### **9. What is the node list for this graph?**
The **node list** simply lists all the vertices:
- `1, 2, 3, 4, 5, 6, 7, 8`.

---

### **10. What is the adjacency matrix for this graph?**
The **adjacency matrix** shows which nodes are connected. If there’s an edge from node \( i \) to node \( j \), the cell at row \( i \), column \( j \) is `1`. If there’s no edge, it’s `0`.

For this graph:

|     | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **1** | 0   | 1   | 0   | 0   | 1   | 0   | 0   | 0   |
| **2** | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   |
| **3** | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   |
| **4** | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| **5** | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   |
| **6** | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   |
| **7** | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   |
| **8** | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   |

---

This concludes the analysis of the graph!
