def compliance_score(plan, rules):
    violations = 0

    if plan["height"] > rules["max_height"]:
        violations += 1
    if plan["fsi"] > rules["max_fsi"]:
        violations += 1

    return max(0.0, 1.0 - violations / 2)
