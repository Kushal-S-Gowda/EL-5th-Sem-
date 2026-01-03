from shapely.geometry import Polygon
import math

def generate_rectangular_masterplan(contract):
    layout = {
        "roads": [],
        "residential_plots": [],
        "commercial_plots": [],
        "parks": []
    }

    LAND_W = contract["land_width"]
    LAND_H = contract["land_height"]

    MAIN_W = contract["main_road_width"]
    INT_W = contract["internal_road_width"]

    # -------------------------
    # Roads (grid)
    # -------------------------
    vx = [LAND_W / 3, 2 * LAND_W / 3]
    hy = [LAND_H / 3, 2 * LAND_H / 3]

    for x in vx:
        layout["roads"].append(Polygon([
            (x, 0), (x + INT_W, 0),
            (x + INT_W, LAND_H), (x, LAND_H)
        ]))

    for y in hy:
        layout["roads"].append(Polygon([
            (0, y), (LAND_W, y),
            (LAND_W, y + INT_W), (0, y + INT_W)
        ]))

    # -------------------------
    # Park (AI-sized)
    # -------------------------
    park_h = LAND_H * contract["green_ratio"] * contract["park_compactness"]
    park = Polygon([
        (vx[0] + INT_W, LAND_H - park_h),
        (vx[1], LAND_H - park_h),
        (vx[1], LAND_H),
        (vx[0] + INT_W, LAND_H)
    ])
    layout["parks"].append(park)

    # -------------------------
    # Commercial (main road)
    # -------------------------
    layout["commercial_plots"].append(
        Polygon([
            (0, 0),
            (vx[0], 0),
            (vx[0], hy[0]),
            (0, hy[0])
        ])
    )

    # -------------------------
    # Residential plots (AI sized)
    # -------------------------
    plot_id = 1
    area = contract["avg_plot_area"] / 10000  # sqm → normalized
    aspect = contract["plot_aspect_ratio"]

    w = math.sqrt(area * aspect)
    h = area / w

    x_start = vx[1] + INT_W
    y_start = 0

    x = x_start
    y = y_start

    while y + h < hy[0] and x + w < LAND_W:
        layout["residential_plots"].append({
            "id": plot_id,
            "geometry": Polygon([
                (x, y),
                (x + w, y),
                (x + w, y + h),
                (x, y + h)
            ]),
            "width_m": round(w * 100, 1),
            "depth_m": round(h * 100, 1),
            "area_sqm": round(w * h * 10000, 1),
            "height_allowed": contract["max_height"]
        })
        plot_id += 1
        y += h + 0.01

        if y + h > hy[0]:
            y = y_start
            x += w + 0.01

    return layout
