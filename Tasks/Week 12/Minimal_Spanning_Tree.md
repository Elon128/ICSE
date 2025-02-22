# Minimal Spanning Tree (MST) Solution

## Graph Details
The graph contains the following vertices and edges with weights:

- Vertices: a, b, c, d, e, f, g, h, i
- Edges with weights:
  - (a, b): 4
  - (a, h): 8
  - (b, h): 11
  - (b, c): 8
  - (c, i): 2
  - (c, d): 7
  - (c, g): 4
  - (d, e): 9
  - (d, f): 14
  - (e, f): 10
  - (f, g): 2
  - (g, i): 5
  - (h, i): 7
  - (h, g): 1

## Minimum Spanning Tree Computation
Using Kruskal's algorithm:
1. Sort all edges by weight in ascending order.
2. Start adding edges to the MST from the smallest weight, ensuring no cycles are formed.
3. Stop when there are `V-1` edges in the MST (where `V` is the number of vertices).

### Edges in the MST
The edges in the MST are:
- (h, g): 1
- (c, i): 2
- (f, g): 2
- (c, g): 4
- (a, b): 4
- (c, d): 7
- (h, i): 7
- (d, e): 9

### Total Weight of MST
The sum of the weights of all edges in the MST is:
1 + 2 + 2 + 4 + 4 + 7 + 7 + 9 = **36**

## Conclusion
The minimum spanning tree for the given graph has a total weight of **36**.
