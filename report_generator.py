def generate_match_report(user, destination, weights):
    # Filter: Check location type (local/foreign)
    if destination["type"] != user["location_type"]:
        return None

    # Filter: Visa requirement (if foreign and user has no visa)
    if user["location_type"] == "foreign" and destination["visa_required"] and not user["has_visa"]:
        return None

    report = {
        "name": destination["name"],
        "score": 0,
        "cost_per_person": destination["cost_per_person"],
        "matched": [],
        "mismatched": []
    }

    score = 0

    # Budget Match
    min_cost, max_cost = destination["cost_per_person"]
    if min_cost <= user["budget"] or max_cost <= user["budget"]:
        score += weights.get("budget", 0)
        report["matched"].append(f"Within Your Budget: ₹{min_cost} - ₹{max_cost}")
    else:
        extra = min_cost - user["budget"]
        report["mismatched"].append(f"Budget Issue: Needs approx ₹{extra} extra")

    # Group Type Match
    if user["group_type"] in destination["group_type"]:
        score += weights.get("group_type", 0)
        report["matched"].append(f"Suitable for {user['group_type']} travelers")
    else:
        report["mismatched"].append(f"Not ideal for {user['group_type']} travelers")

    # Purpose Match
    if user["purpose"].lower() in [p.lower() for p in destination["purpose"]]:
        score += weights.get("purpose", 0)
        report["matched"].append(f"Perfect for {user['purpose']} purposes")
    else:
        report["mismatched"].append(f"Not ideal for {user['purpose']} purpose")

    # Month Match
    month = user["month"]
    if month in destination["ideal_months"]:
        score += weights.get("month", 0)
        reason = destination.get("month_reasons", {}).get(month, "Best time to visit")
        report["matched"].append(f"Ideal month: {month} ({reason})")

    if month in destination.get("not_ideal_months", []):
        score -= 5  # You can customize penalty
        reason = destination.get("month_reasons", {}).get(month, "Weather or activity limitations")
        report["mismatched"].append(f"Not ideal in {month}: {reason}")

    # Visa Note (Informational only — filtering was done earlier)
    if user["location_type"] == "foreign":
        if destination["visa_required"]:
            report["matched"].append("Visa required – You have it ✅")
        else:
            report["matched"].append("No visa required")

    # Final Score
    report["score"] = score
    return report


def generate_reports(user, destinations, weights):
    reports = []

    for destination in destinations:
        report = generate_match_report(user, destination, weights)
        if report:
            reports.append(report)

    return reports
