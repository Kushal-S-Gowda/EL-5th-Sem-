import numpy as np

def apply_ca(cells):
    grid = np.random.rand(len(cells)) > 0.35

    for i, cell in enumerate(cells):
        cell["buildable"] = bool(grid[i])

    return cells


def cluster_buildable_cells(cells):
    clusters = []
    current = []

    for c in cells:
        if c.get("buildable", False):
            current.append(c["geometry"])
        elif current:
            clusters.append(current)
            current = []

    if current:
        clusters.append(current)

    return clusters
