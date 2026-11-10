# Architecture

`main.py` loads the CSV data in `data/`, builds one weighted graph, runs every algorithm module, then writes charts and the dashboard.

```text
data/*.csv --> src/graph.py (Graph, MinHeap, CSV loader)
                 |-- src/mst.py        Prim, Kruskal (union-find)
                 |-- src/sssp.py       Dijkstra, Bellman-Ford
                 |-- src/apsp.py       Floyd-Warshall
                 |-- src/tsp.py        nearest neighbour, Held-Karp, tour cost
                 '-- src/wait_model.py MST preorder tour, loop time, average wait
data/shifts.csv --> src/greedy.py      interval scheduling, driver assignment
data/demand.csv, fleet.csv --> src/dp.py   0-1 knapsack
wait_model --> src/sensitivity.py      wait vs number of shuttles
src/experiments.py                     runtime benchmark on random graphs
src/dashboard.py + dashboard_template.html --> report/dashboard.html --> docs/index.html
```

Design choices: plain Python (no graph library) so every algorithm is readable; each module has independent cross-checks in `tests/`; the dashboard is one offline HTML file with the real results injected as JSON, so it can be hosted as a static page.
