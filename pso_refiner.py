def refine(best):
    best["road_width_main"] *= 0.95
    best["road_width_internal"] *= 1.05
    best["plot_aspect_ratio"] = min(max(best["plot_aspect_ratio"], 1.2), 2.0)
    best["avg_plot_area"] *= 0.98
    return best
