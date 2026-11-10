# Algorithms

| Algorithm | File | Idea in one line | Time |
|---|---|---|---|
| Prim | `src/mst.py` | Grow a tree from one stop, always adding the cheapest edge leaving it | O(E log V) |
| Kruskal | `src/mst.py` | Sort edges, add each one that does not form a cycle (union-find) | O(E log E) |
| Dijkstra | `src/sssp.py` | Settle the closest unsettled stop first (min-heap) | O((V+E) log V) |
| Bellman-Ford | `src/sssp.py` | Relax every edge V-1 times; also detects negative cycles | O(VE) |
| Floyd-Warshall | `src/apsp.py` | Allow one more intermediate stop at a time (DP over all pairs) | O(V³) |
| Interval scheduling | `src/greedy.py` | Take the shift that finishes earliest | O(S log S) |
| 0-1 knapsack | `src/dp.py` | Best passenger value for each seat count, then trace back chosen groups | O(nW) |
| Nearest neighbour | `src/tsp.py` | Always go to the closest unvisited stop | O(n²) |
| MST preorder tour | `src/wait_model.py` | Walk the MST depth-first: a 2-approximation of the best tour | O(V log V) |
| Held-Karp | `src/tsp.py` | Exact TSP by DP over subsets of stops | O(n² 2ⁿ) |

Each result is cross-checked in `tests/test_algorithms.py` (for example Prim vs Kruskal, Held-Karp vs brute force).
