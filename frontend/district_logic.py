from shapely.geometry import Point

def assign_districts(blocks, center):
    output = []

    for b in blocks:
        d = b["geometry"].centroid.distance(center)

        if d < 0.15:
            zone = "CBD"
            landuse = "commercial"
            height_factor = 1.0
        elif d < 0.35:
            zone = "MID"
            landuse = "mixed"
            height_factor = 0.7
        else:
            zone = "OUTER"
            landuse = "residential"
            height_factor = 0.4

        output.append({
            **b,
            "zone": zone,
            "landuse": landuse,
            "height_factor": height_factor
        })

    return output
