from destination_list import destinations

reports = []

user = {
    "location_type": "foreign",     # User prefers foreign destinations
    "has_visa": True,               # User has a visa
    "budget": 45000,                # Budget in INR
    "group_type": "friends",        # Traveling with friends
    "purpose": "adventure",         # Main purpose of the trip
    "month": "December"            # Preferred travel month
}



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
    if destination["cost_per_person"][0] <= user["budget"] <= destination["cost_per_person"][1]:
        score += 10
        report["matched"].append("Within budget")
    else:
        diff = destination["cost_per_person"][0] - user["budget"]
        report["mismatched"].append(f"Not Within Budget, If you can manage per person: {diff}")
    
    # Group type checking
    if user["group_type"] in destination["group_type"]:
        score += 10
        report["matched"].append("Group Type Matched")
    else:
        report["mismatched"].append(f"Not much ideal for {user['group_type']} groups")
    
    # Visa Checking 
    if destination["visa_required"]:
        report["matched"].append("Visa Requirements Match")
    else:
        report["mismatched"].append("Visa Requirements Doesn't Match")
        
    # Location Type Checking
    if destination["type"] == "foreign":
        report["matched"].append("Foreign Location")
    else:
        report["mismatched"].append("Indian Location")
        
    # Purpose Checking
    if user["purpose"] in [p.lower() for p in destination["purpose"]]:  # Normalize case
        score += 10
        report["matched"].append(f"Ideal location for {user['purpose']}")
    else:
        report["mismatched"].append(f"Not ideal location for {user['purpose']}")
    
    # Month Checking
    if user["month"] in destination["ideal_months"]:
        score += 10
        report["matched"].append(destination["month_reasons"].get(user["month"], "Good month for travel"))
    
    if user["month"] in destination["not_ideal_months"]:
        score -= 10
        report["mismatched"].append(destination["month_reasons"].get(user["month"], "Not ideal month for travel"))
    
    #Add the final score to the report
    report["score"] = score
    
    
    #Add the cost per person 
    report["cost_per_person"] = destination["cost_per_person"]
    return report    




#This is a function to generate reports for all destinations
def generate_reports():
    for dest in destinations:
        report = generate_match_report(user, dest)
        if report:
            reports.append(report)
            




#This is the function that generates the reports with the highest score
def get_best_reports():
    
    #Sort all reports
    if len(reports) > 0: 
        sorted_reports = sorted(
            reports, 
            key=lambda report: (
                -report["score"], #Descending by score
                report["cost_per_person"][0], #Then ascending cost per person
                -len(report["matched"]) #Then descending by number of points that matched
            )   
        )
    
        highest_score = sorted_reports[0]["score"]
        
        top_reports = []
        for single_report in sorted_reports:
            
            if(single_report["score"] == highest_score):
                top_reports.append(single_report)
                
        return top_reports    
    
    return []

top_reports = get_best_reports()
def display_report_to_user():
    
    
    #If no reports are generated
    if len(top_reports) <= 0:
        print("We found no matches for destination based on your input")
        return
    
    
    print(f"Based on your input, {len(top_reports)} destinations are shortlisted")
    
    cnt = 1
    
    for report in top_reports:
        print(f"You are on {cnt}/{len(top_reports)}")
        
        print(f"Destination: {report["name"]}")
        print("Why We have suggest you this destination")
        
        for i in range(len(report["matched"])):
            print(f"{i + 1}. {report["matched"][i]}")
            
        print("But you should also note down that")
        for i in range(len(report["mismatched"])):
            print(f"{i + 1}. {report["mismatched"][i]}")
            
            
        