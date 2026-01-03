from shapely.geometry import LineString

def generate_roads(boundary, spacing=0.08):
    minx, miny, maxx, maxy = boundary.bounds
    roads = []

    x = minx
    while x < maxx:
        roads.append(LineString([(x, miny), (x, maxy)]))
        x += spacing

    y = miny
    while y < maxy:
        roads.append(LineString([(minx, y), (maxx, y)]))
        y += spacing

    return roads
