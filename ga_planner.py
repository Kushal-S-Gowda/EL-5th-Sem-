import random
import copy
from fitness_engine import evaluate

class GAPlanner:
    def __init__(self, population, rules, weights):
        self.population = population
        self.rules = rules
        self.weights = weights

    def crossover(self, p1, p2):
        return {
            "fsi": (p1["fsi"] + p2["fsi"]) / 2,
            "height": (p1["height"] + p2["height"]) / 2,
            "green_ratio": (p1["green_ratio"] + p2["green_ratio"]) / 2,
            "density": (p1["density"] + p2["density"]) / 2,
        }

    def mutate(self, p):
        p["fsi"] += random.uniform(-0.3, 0.3)
        p["height"] += random.uniform(-3, 3)
        p["green_ratio"] += random.uniform(-0.05, 0.05)
        p["density"] += random.uniform(-0.1, 0.1)

        p["fsi"] = max(1.0, min(p["fsi"], self.rules["max_fsi"]))
        p["height"] = max(6, min(p["height"], self.rules["max_height"]))
        p["green_ratio"] = max(0.15, min(p["green_ratio"], 0.45))
        p["density"] = max(0.2, min(p["density"], 0.8))
        return p

    def evolve(self, generations=25):
        for _ in range(generations):
            scored = [(evaluate(p, self.rules, self.weights), p) for p in self.population]
            scored.sort(reverse=True, key=lambda x: x[0])
            self.population = [p for _, p in scored[:len(scored)//2]]

            while len(self.population) < len(scored):
                p1, p2 = random.sample(self.population, 2)
                self.population.append(self.mutate(self.crossover(p1, p2)))

        best = max(self.population, key=lambda p: evaluate(p, self.rules, self.weights))

        # 🔹 GA → GEOMETRY DRIVERS
        return {
            "fsi": best["fsi"],
            "max_height": best["height"],
            "green_ratio": best["green_ratio"],

            "avg_plot_area": 120 + best["fsi"] * 40,     # sqm
            "plot_aspect_ratio": 1.4 + (best["fsi"] - 1) * 0.1,
            "road_width_main": 18 + best["fsi"] * 2,     # meters
            "road_width_internal": 9 + best["fsi"],
            "park_compactness": 0.6 + best["green_ratio"],
            "density": best["density"]
        }
