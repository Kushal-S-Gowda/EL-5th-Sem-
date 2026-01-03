from shapely.geometry import Polygon
import uuid

def generate_planning_cells(boundary, grid_size=20):
    minx, miny, maxx, maxy = boundary.bounds
    dx = (maxx - minx) / grid_size
    dy = (maxy - miny) / grid_size

    cells = []
    cell_id = 0

    for i in range(grid_size):
        for j in range(grid_size):
            x0 = minx + i * dx
            y0 = miny + j * dy
            x1 = x0 + dx
            y1 = y0 + dy

            poly = Polygon([
                (x0, y0),
                (x1, y0),
                (x1, y1),
                (x0, y1)
            ])

            cells.append({
                "id": cell_id,
                "geometry": poly,
                "buildable": True  # CA will overwrite
            })

            cell_id += 1

    return cells
