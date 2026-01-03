from shapely.geometry import Polygon
import random

# plot sizes in meters (scaled units)
PLOT_TYPES = [
    (0.03, 0.04),  # 30x40
    (0.03, 0.045), # 30x45
    (0.03, 0.05)   # 30x50
]

def subdivide_block(block_poly):
    minx, miny, maxx, maxy = block_poly.bounds
    plots = []

    y = miny
    plot_id = 1

    while y < maxy:
        x = minx
        w, h = random.choice(PLOT_TYPES)

        while x + w <= maxx:
            if y + h <= maxy:
                plots.append({
                    "id": plot_id,
                    "geometry": Polygon([
                        (x, y),
                        (x+w, y),
                        (x+w, y+h),
                        (x, y+h)
                    ]),
                    "size": f"{int(w*1000)}×{int(h*1000)}"
                })
                plot_id += 1
            x += w
        y += h

    return plots
