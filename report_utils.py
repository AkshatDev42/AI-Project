
#This is the function that generates the reports with the highest score
def get_best_reports(reports):
    
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



def display_report_to_user(top_reports):
    
    
    #If no reports are generated
    if len(top_reports) <= 0:
        print("We found no matches for destination based on your input")
        return
    
    
    print(f"Based on your input, {len(top_reports)} destinations are shortlisted")
    
    cnt = 1
    
    for report in top_reports:
        print(f"You are on {cnt}/{len(top_reports)}")
        
        print(f"Destination: {report['name']}")
        
        if len(report["matched"]) > 0:
            print("Why We have suggest you this destination")
            for i in range(len(report["matched"])):
                print(f"{i + 1}. {report['matched'][i]}")
            
        
        if len(report["mismatched"]) > 0:
            print("But you should also note down that")
            for i in range(len(report["mismatched"])):
                print(f"{i + 1}. {report['mismatched'][i]}")
            
            
        if(cnt != len(top_reports)):
            continue_watching = input("Do you want to see the next destination?")
            
            if(continue_watching == "No" or continue_watching == "N"):
                break
        
            cnt += 1
            
      