from shapely.geometry import Polygon
from spatial_units import generate_planning_cells
from ca_morphology import apply_ca, cluster_buildable_cells
from ga_planner import GAPlanner
from pso_refiner import refine
from output_contract import build_layout_contract

def run_pipeline():
    # ----------------------------------
    # 1. Boundary (synthetic for now)
    # ----------------------------------
    boundary = Polygon([(0,0),(1,0),(1,1),(0,1)])

    # ----------------------------------
    # 2. CA – spatial suitability
    # ----------------------------------
    cells = generate_planning_cells(boundary)
    cells = apply_ca(cells)
    clusters = cluster_buildable_cells(cells)

    # ----------------------------------
    # 3. GA setup
    # ----------------------------------
    rules = {"max_height": 45, "max_fsi": 4.0}
    weights = {
        "compliance": 0.4,
        "mobility": 0.2,
        "sustainability": 0.2,
        "economic": 0.1,
        "density": 0.1
    }

    population = []
    for _ in range(30):
        population.append({
            "fsi": 2.0,
            "height": 18,
            "green_ratio": 0.3,
            "density": 0.5
        })

    # ----------------------------------
    # 4. GA + PSO
    # ----------------------------------
    best = GAPlanner(population, rules, weights).evolve()
    best = refine(best)

    # ----------------------------------
    # 5. Build geometry contract
    # ----------------------------------
    contract = build_layout_contract(best, clusters)

    return contract
