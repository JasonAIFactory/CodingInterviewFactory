"""
07_topological_sort.py  —  REFERENCE FILE

Topological Sort template.

Use when:
  - Tasks with dependencies / prerequisites
  - "Course Schedule" type problems
  - Build order

Only works on a DAG (Directed Acyclic Graph).
If a cycle exists, no topo order is possible.

Two algorithms:
  1. Kahn's algorithm (BFS-based, with in-degree counts)
  2. DFS-based (post-order then reverse)
"""

from collections import defaultdict, deque


# ============================================================
# 1. Kahn's algorithm — BFS based
# ============================================================

def topo_sort_kahn(num_nodes: int, edges: list[list[int]]) -> list[int]:
    """
    edges: list of [u, v] meaning u must come before v.
    Returns a valid topological order, or [] if a cycle exists.
    """
    graph: dict[int, list[int]] = defaultdict(list)
    indegree: list[int] = [0] * num_nodes
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue: deque[int] = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == num_nodes else []     # [] = cycle exists


# ============================================================
# 2. DFS-based topological sort
# ============================================================

def topo_sort_dfs(num_nodes: int, edges: list[list[int]]) -> list[int]:
    graph: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    state: list[int] = [WHITE] * num_nodes
    order: list[int] = []
    has_cycle = False

    def dfs(node: int) -> None:
        nonlocal has_cycle
        if has_cycle:
            return
        state[node] = GRAY
        for nxt in graph[node]:
            if state[nxt] == GRAY:        # back edge → cycle
                has_cycle = True
                return
            if state[nxt] == WHITE:
                dfs(nxt)
        state[node] = BLACK
        order.append(node)

    for i in range(num_nodes):
        if state[i] == WHITE:
            dfs(i)

    return list(reversed(order)) if not has_cycle else []


# ============================================================
# 3. Course Schedule — can finish? (just detect cycle)
# ============================================================

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Each [a, b] means b is a prerequisite for a."""
    edges = [[b, a] for a, b in prerequisites]          # b -> a
    return len(topo_sort_kahn(num_courses, edges)) == num_courses


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    # 0 → 1, 0 → 2, 1 → 3, 2 → 3
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    print(topo_sort_kahn(4, edges))                     # e.g. [0, 1, 2, 3]
    print(topo_sort_dfs(4, edges))                      # e.g. [0, 2, 1, 3]

    # Cycle 0 → 1 → 0
    cyc = [[0, 1], [1, 0]]
    print(topo_sort_kahn(2, cyc))                       # []
    print(topo_sort_dfs(2, cyc))                        # []

    print(can_finish(2, [[1, 0]]))                      # True
    print(can_finish(2, [[1, 0], [0, 1]]))              # False
