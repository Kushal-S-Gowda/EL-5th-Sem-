def build_layout_contract(best, clusters):
    """
    This contract is the ONLY interface between:
    AI Core (CA + GA + PSO)  →  Geometry Engine (2D / 3D)
    """

    # -------------------------
    # Base land dimensions
    # -------------------------
    land_width = 1.0
    land_height = 1.0

    # -------------------------
    # Derive plot count from CA + GA density
    # -------------------------
    buildable_cells = sum(len(c) for c in clusters) if clusters else 0
    target_plots = max(20, int(buildable_cells * best["density"]))

    # -------------------------
    # Plot size mix driven by GA
    # -------------------------
    plot_mix = {
        (0.06, 0.08): 0.4,   # small plots
        (0.08, 0.10): 0.4,   # medium plots
        (0.10, 0.12): 0.2    # large plots
    }

    return {
        # -------------------------
        # LAND
        # -------------------------
        "land_width": land_width,
        "land_height": land_height,

        # -------------------------
        # ROADS (PSO-refined)
        # -------------------------
        "main_road_width": best["road_width_main"] / 100,
        "internal_road_width": best["road_width_internal"] / 100,

        # -------------------------
        # PARKS
        # -------------------------
        "green_ratio": best["green_ratio"],
        "park_compactness": best["park_compactness"],

        # -------------------------
        # RESIDENTIAL
        # -------------------------
        "avg_plot_area": best["avg_plot_area"],
        "plot_aspect_ratio": best["plot_aspect_ratio"],
        "target_plot_count": target_plots,
        "plot_size_mix": plot_mix,

        # -------------------------
        # REGULATIONS
        # -------------------------
        "max_height": best["max_height"],
        "fsi": best["fsi"],

        # -------------------------
        # CA OUTPUT (for future block shaping)
        # -------------------------
        "ca_clusters": clusters
    }
