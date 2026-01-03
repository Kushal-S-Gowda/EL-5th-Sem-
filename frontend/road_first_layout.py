from shapely.geometry import Polygon

def generate_road_first_layout(boundary):
    minx, miny, maxx, maxy = boundary.bounds

    layout = {
        "roads": [],
        "residential": [],
        "commercial": [],
        "parks": []
    }

    # =========================
    # 1️⃣ ROADS AS POLYGONS
    # =========================

    # Main road (60 ft)
    main_road = Polygon([
        (minx, 0.48),
        (maxx, 0.48),
        (maxx, 0.58),
        (minx, 0.58)
    ])

    # Internal road (30 ft)
    inner_road = Polygon([
        (0.15, 0.20),
        (0.85, 0.20),
        (0.85, 0.26),
        (0.15, 0.26)
    ])

    layout["roads"] = [
        ("main", main_road),
        ("internal", inner_road)
    ]

    # =========================
    # 2️⃣ PARK (BIG & CENTRAL)
    # =========================
    park = Polygon([
        (0.30, 0.62),
        (0.70, 0.62),
        (0.70, 0.90),
        (0.30, 0.90)
    ])
    layout["parks"].append(park)

    # =========================
    # 3️⃣ COMMERCIAL BLOCK
    # =========================
    x = 0.10
    plot_id = 1
    while x + 0.10 <= 0.90:
        layout["commercial"].append({
            "id": plot_id,
            "geometry": Polygon([
                (x, 0.40),
                (x + 0.10, 0.40),
                (x + 0.10, 0.48),
                (x, 0.48)
            ])
        })
        plot_id += 1
        x += 0.11

    # =========================
    # 4️⃣ RESIDENTIAL BLOCKS
    # =========================
    def residential_strip(y_start, rows=2):
        nonlocal plot_id
        y = y_start
        for _ in range(rows):
            x = 0.10
            while x + 0.08 <= 0.90:
                layout["residential"].append({
                    "id": plot_id,
                    "geometry": Polygon([
                        (x, y),
                        (x + 0.08, y),
                        (x + 0.08, y + 0.10),
                        (x, y + 0.10)
                    ])
                })
                plot_id += 1
                x += 0.09
            y += 0.11

    residential_strip(0.05, rows=1)
    residential_strip(0.28, rows=1)

    return layout
