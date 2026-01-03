from rule_engine_proxy import compliance_score
from simulation_proxy import mobility_score

def evaluate(plan, rules, weights):
    compliance = compliance_score(plan, rules)
    mobility = mobility_score(plan)

    sustainability = plan["green_ratio"]
    economic = plan["fsi"] / rules["max_fsi"]

    return (
        weights["compliance"] * compliance +
        weights["mobility"] * mobility +
        weights["sustainability"] * sustainability +
        weights["economic"] * economic
    )
