# Shortest Path Tree (SPT) Solution

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

## Shortest Path Tree Computation
Using Dijkstra's algorithm:
1. Start from a chosen source vertex (e.g., vertex `a`) and initialize distances to all other vertices as infinity, except the source which has a distance of 0.
2. Update the distances to the neighboring vertices by relaxing the edges.
3. Continue until the shortest distances to all vertices are found.

### Shortest Path Tree Edges and Weights
The edges included in the shortest path tree (SPT) are:
- (a, b): 4
- (a, h): 8
- (h, g): 1
- (c, i): 2
- (c, d): 7
- (f, g): 2
- (d, e): 9

### Sum of Weights in the Shortest Path Tree
The total sum of weights in the SPT is:
4 + 8 + 1 + 2 + 7 + 2 + 9 = **33**

## Conclusion
The shortest path tree for the given graph has a total weight of **33**.
