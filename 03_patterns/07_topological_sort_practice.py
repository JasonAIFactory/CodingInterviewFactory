"""
07_topological_sort_practice.py  —  TYPE FROM SCRATCH
"""

from collections import defaultdict, deque


# ============================================================
# 1. topo_sort_kahn(num_nodes, edges) -> list[int]   ([] if cycle)
# ============================================================

def topo_sort_kahn(num_nodes, edges):
    # TODO: build graph + indegree[]
    # TODO: queue = nodes with indegree 0
    # TODO: while queue: pop, append, decrement neighbors' indegree, enqueue if 0
    # TODO: if len(order) < num_nodes -> cycle, return []
    pass


# ============================================================
# 2. topo_sort_dfs(num_nodes, edges) -> list[int]   ([] if cycle)
# ============================================================

def topo_sort_dfs(num_nodes, edges):
    # TODO: build graph
    # TODO: state colors WHITE / GRAY / BLACK
    # TODO: dfs marks GRAY, recurses (back edge if GRAY -> cycle), marks BLACK, appends
    # TODO: return reversed order, or [] if cycle
    pass


# ============================================================
# 3. can_finish(num_courses, prerequisites) -> bool
# prerequisites[i] = [a, b] means b is prerequisite for a
# ============================================================

def can_finish(num_courses, prerequisites):
    # TODO: convert to edges b -> a
    # TODO: use topo_sort_kahn; success if returned len == num_courses
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    order = topo_sort_kahn(4, edges)
    assert len(order) == 4
    pos = {v: i for i, v in enumerate(order)}
    for u, v in edges:
        assert pos[u] < pos[v]            # u comes before v

    order_dfs = topo_sort_dfs(4, edges)
    assert len(order_dfs) == 4
    pos2 = {v: i for i, v in enumerate(order_dfs)}
    for u, v in edges:
        assert pos2[u] < pos2[v]

    assert topo_sort_kahn(2, [[0, 1], [1, 0]]) == []
    assert topo_sort_dfs(2, [[0, 1], [1, 0]]) == []

    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False

    print("✅ All tests passed.")
