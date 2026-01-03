from shapely.ops import unary_union
from shapely.geometry import Polygon, MultiPolygon

def generate_blocks(cells):
    polygons = []

    for c in cells:
        if c["buildable"]:
            poly = c["polygon"]
            if isinstance(poly, Polygon):
                polygons.append(poly)

    if not polygons:
        return []

    merged = unary_union(polygons)

    blocks = []

    # Case 1: single Polygon
    if isinstance(merged, Polygon):
        blocks.append({
            "geometry": merged,
            "area": merged.area
        })

    # Case 2: MultiPolygon
    elif isinstance(merged, MultiPolygon):
        for poly in merged.geoms:
            blocks.append({
                "geometry": poly,
                "area": poly.area
            })

    return blocks
