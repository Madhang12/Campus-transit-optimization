"""Draws extra charts from the project's REAL algorithm output (no typed-in numbers).
Run from the repo root:  python scripts/make_figures.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from src import mst, wait_model
from src.graph import Graph

OUT = pathlib.Path("report/figures"); OUT.mkdir(parents=True, exist_ok=True)
g = Graph.from_csv()
by_name = {n: v for v, n in g.names.items()}
src = by_name["Bus Stop"]
pe, _ = mst.prim(g)
w = wait_model.compare(g, pe, src)

# 1. Campus network with the MST highlighted
fig, ax = plt.subplots(figsize=(7, 6))
mst_set = {frozenset((u, v)) for u, v, *_ in pe}
for u, v, *_ in g.edges():
    (la1, lo1), (la2, lo2) = g.coords[u], g.coords[v]
    on = frozenset((u, v)) in mst_set
    ax.plot([lo1, lo2], [la1, la2], color="#0f766e" if on else "#cbd5e1", lw=2.5 if on else 1, zorder=1)
for v, (la, lo) in g.coords.items():
    ax.scatter(lo, la, s=40, color="#0f172a", zorder=2)
    ax.annotate(g.names[v], (lo, la), fontsize=7, xytext=(3, 3), textcoords="offset points")
ax.ticklabel_format(useOffset=False, style="plain"); ax.tick_params(labelsize=7)
ax.set_title("Campus road network (teal = minimum spanning tree)")
ax.set_xlabel("longitude"); ax.set_ylabel("latitude")
fig.tight_layout(); fig.savefig(OUT / "campus_network_mst.png", dpi=150); plt.close(fig)

# 2. Tour cost comparison
names, costs = list(w["costs"]), list(w["costs"].values())
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(names, costs, color=["#dc2626", "#64748b", "#64748b", "#0f766e"][:len(names)])
ax.bar_label(bars, fmt="%.2f")
ax.set_ylabel("closed tour time (min)"); ax.set_title("Tour cost by method (lower is better)")
plt.xticks(rotation=15); fig.tight_layout(); fig.savefig(OUT / "tour_cost_comparison.png", dpi=150); plt.close(fig)

# 3. Waiting time, step by step
labels = ["1 shuttle\nfile order", "1 shuttle\nMST tour", "3 shuttles\nMST slices"]
vals = [w["before"], w["route_only"], w["after"]]
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(labels, vals, color=["#dc2626", "#64748b", "#0f766e"])
ax.bar_label(bars, fmt="%.2f")
ax.set_ylabel("average wait (min)"); ax.set_title("Average passenger wait (modelled, estimated data)")
fig.tight_layout(); fig.savefig(OUT / "wait_comparison.png", dpi=150); plt.close(fig)
print("saved", *sorted(p.name for p in OUT.glob("*.png")))
