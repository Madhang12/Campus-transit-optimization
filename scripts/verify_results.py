"""Re-computes the headline numbers and checks them against the reported values.
Run from the repo root:  python scripts/verify_results.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src import mst, wait_model
from src.graph import Graph

g = Graph.from_csv()
src = {n: v for v, n in g.names.items()}["Bus Stop"]
pe, pw = mst.prim(g); ke, kw = mst.kruskal(g)
w = wait_model.compare(g, pe, src)
c = w["costs"]
checks = [
    ("Prim MST total = 5.81", round(pw, 2) == 5.81),
    ("Kruskal total equals Prim", abs(pw - kw) < 1e-9),
    ("Held-Karp tour = 9.92", round(c["Optimal (Held-Karp)"], 2) == 9.92),
    ("Nearest neighbour tour = 10.11", round(c["Nearest neighbour"], 2) == 10.11),
    ("MST preorder tour = 10.11", round(c["MST preorder"], 2) == 10.11),
    ("File-order tour = 13.37", round(c["File order"], 2) == 13.37),
    ("Baseline wait ~ 6.69 (6.685)", abs(w["before"] - 6.685) < 0.005),
    ("MST-tour wait ~ 5.05", abs(w["route_only"] - 5.055) < 0.006),
    ("3-shuttle wait = 2.03", round(w["after"], 2) == 2.03),
    ("Improvement rounds to 70%", round(w["improvement_pct"]) == 70),
    ("MST tour within 2x of optimal", w["mst_ratio"] <= 2.0),
]
for name, ok in checks:
    print(("PASS" if ok else "FAIL"), name)
sys.exit(0 if all(ok for _, ok in checks) else 1)
