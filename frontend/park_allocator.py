from shapely.geometry import Polygon

def allocate_parks(boundary):
    minx, miny, maxx, maxy = boundary.bounds

    park1 = Polygon([
        (minx, maxy*0.65),
        (minx + (maxx-minx)*0.25, maxy*0.65),
        (minx + (maxx-minx)*0.25, maxy),
        (minx, maxy)
    ])

    park2 = Polygon([
        (maxx*0.65, miny),
        (maxx, miny),
        (maxx, miny + (maxy-miny)*0.25),
        (maxx*0.65, miny + (maxy-miny)*0.25)
    ])

    return [park1, park2]
