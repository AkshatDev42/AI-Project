def show_all_destinations(destinations):
    print("Available Destinations")
    i = 1

    destination_names = [dest["name"] for dest in destinations]

    for name in destination_names:
        print(f"{i}. {name}", end = ((20 - len(name)) * " "))    
        if i % 3 == 0:
            print()
        i += 1
        
    print()
    return destination_names


def compare_destinations(destinations, d1, d2):
    dest1 = None
    dest2 = None

    for dest in destinations:
        if dest["name"] == d1:
            dest1 = dest
        elif dest["name"] == d2:
            dest2 = dest

        if dest1 and dest2:
            break

    if not dest1 or not dest2:
        print("❌ One or both destinations not found.")
        return

    print(f"\n📊 Comparison: {dest1['name']} vs {dest2['name']}")
    print(f"💰 Cost per Person: ₹{dest1['cost_per_person']} vs ₹{dest2['cost_per_person']}")
    print(f"🌤 Best Months: {', '.join(dest1['ideal_months'])} vs {', '.join(dest2['ideal_months'])}")
    print(f"🛂 Visa Required: {'Yes' if dest1['visa_required'] else 'No'} for {dest1['name']}vs {'Yes' if dest2['visa_required'] else 'No'} for {dest2["name"]}")
    print(f"👥 Ideal Group: {', '.join(dest1['group_type'])} vs {', '.join(dest2['group_type'])}")
    print(f"🎯 Ideal Purposes: {', '.join(dest1['purpose'])} vs {', '.join(dest2['purpose'])}")
    print()



def get_suggestions_month(destinations, month):
    recommended = []
    avoid = []

    for dest in destinations:
        name = dest["name"]
        month_reasons = dest.get("month_reasons", {})
        reason = month_reasons.get(month, "No specific reason available.")

        if month in dest.get("ideal_months", []):
            recommended.append({
                "name": name,
                "reason": reason,
                "cost": dest["cost_per_person"],
                "group": dest["group_type"],
                "purpose": dest["purpose"],
                "places_to_visit": dest.get("places_to_visit", [])
            })
        elif month in dest.get("not_ideal_months", []):
            avoid.append({
                "name": name,
                "reason": reason
            })

    # Print Recommended
    if recommended:
        print(f"\n🌤 Recommended Destination(s) for {month}:")
        for i, r in enumerate(recommended, 1):
            print(f"{i}. {r['name']}")
            print(f"   - Reason: {r['reason']}")
            print(f"   - Cost per person: ₹{r['cost'][0]}–₹{r['cost'][1]}")
            print(f"   - Ideal Group: {', '.join(r['group'])}")
            print(f"   - Ideal Purposes: {', '.join(r['purpose'])}")
            print(f"   - Places to Visit: {', '.join(r['places_to_visit'])}\n")
    else:
        print(f"\n⚠️ No recommended destinations found for {month}.")

    # Print Avoid
    if avoid:
        print(f"\n🚫 Destinations to Avoid in {month}:")
        for a in avoid:
            print(f"- {a['name']}: {a['reason']}")
    else:
        print(f"\n✅ No major destinations to avoid in {month}.")

    print()


def get_suggestions_budget(destinations, budget):
    recommended = []
    avoid = []

    for dest in destinations:
        min_cost, max_cost = dest.get("cost_per_person", (0, 0))
        name = dest["name"]

        if budget >= min_cost:
            recommended.append({
                "name": name,
                "cost": dest["cost_per_person"],
                "ideal_months": dest.get("ideal_months", []),
                "group": dest.get("group_type", []),
                "purpose": dest.get("purpose", []),
                "places_to_visit": dest.get("places_to_visit", [])
            })
        else:
            avoid.append({
                "name": name,
                "reason": f"Minimum cost ₹{min_cost} is higher than your budget of ₹{budget}"
            })

    # Print Recommended
    if recommended:
        print(f"\n💰 Recommended Destination(s) under your budget (₹{budget}+):")
        for i, r in enumerate(recommended, 1):
            print(f"{i}. {r['name']}")
            print(f"   - Cost per person: ₹{r['cost'][0]}–₹{r['cost'][1]}")
            print(f"   - Best Months: {', '.join(r['ideal_months'])}")
            print(f"   - Ideal Group: {', '.join(r['group'])}")
            print(f"   - Ideal Purposes: {', '.join(r['purpose'])}")
            print(f"   - Places to Visit: {', '.join(r['places_to_visit'])}\n")
    else:
        print(f"\n⚠️ No destinations found within your budget of ₹{budget}.")

    # Print Avoid
    if avoid:
        print(f"\n🚫 Destinations Too Costly for Your Budget:")
        for a in avoid:
            print(f"- {a['name']}: {a['reason']}")
    else:
        print(f"\n✅ No destinations to avoid based on your budget.")
