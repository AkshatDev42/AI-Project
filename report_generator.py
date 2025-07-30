#This is a function to generate report of single destination
def generate_match_report(user, destination):
    if destination["type"] != user["location_type"]:
        return None
    
    if user["location_type"] != "local" and destination["visa_required"] and not user["has_visa"]:
        return None
    
    report = {
        "name": destination["name"],
        "score": 0,
        "cost_per_person": 0,
        "matched": [],
        "mismatched": []
    }
    
    score = 0
    
    # Budget Checking
    if destination["cost_per_person"][0] <= user["budget"] or destination["cost_per_person"][1] <= user["budget"]:
        score += 10
        report["matched"].append(f"Within Your Budget Usually: {destination["cost_per_person"][0]} to {destination["cost_per_person"][1]}")
    else:
        diff = destination["cost_per_person"][0] - user["budget"]
        report["mismatched"].append(f"Not Within Budget, If you can manage extra per person: {diff}")
    
    # Group type checking
    if user["group_type"] in destination["group_type"]:
        score += 10
        report["matched"].append(f"Ideal for visiting for {user['group_type']} travel")
    else:
        report["mismatched"].append(f"Not much ideal for {user['group_type']} travel")
    
    # Visa Checking 
    if user["location_type"] == "foreign":
        if destination["visa_required"]:
            if user["has_visa"]:
                report["matched"].append("Visa requirement fulfilled")
            else:
                report["mismatched"].append("Visa required but not available")  # This won't execute due to early return
        else:
            report["matched"].append("No visa required")
        
    # Location Type Checking
    if destination["type"] == "foreign":
        report["matched"].append("Foreign destination")
    else:
        report["matched"].append("Local destination")


    # Purpose Checking
    if user["purpose"] in [p.lower() for p in destination["purpose"]]:  # Normalize case
        score += 10
        report["matched"].append(f"Ideal location for {user['purpose']}")
    else:
        report["mismatched"].append(f"Not ideal location for {user['purpose']}")
    
    # Month Checking
    if user["month"] in destination["ideal_months"]:
        score += 10
        report["matched"].append(f"Ideal for visit in {user["month"]}: {destination["month_reasons"].get(user["month"])}")
    
    if user["month"] in destination["not_ideal_months"]:
        score -= 10
        report["mismatched"].append(f"Not ideal for visit in {user['month']}: {destination["month_reasons"].get(user["month"])}")
    
    #Add the final score to the report
    report["score"] = score
    
    
    #Add the cost per person 
    report["cost_per_person"] = destination["cost_per_person"]
    return report    



def generate_reports(user, destinations):
    reports = []
    for dest in destinations:
        report = generate_match_report(user, dest)
        if report:
            reports.append(report)

    return reports
            
