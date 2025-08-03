from user_weights_input import get_weight_preferences

def get_user_input():
    print("Please answer a few questions: \n")

    location_type = input("Do you want to travel locally or to a foreign location? (local/foreign): ").strip().lower()
    while location_type not in ["local", "foreign"]:
        location_type = input("Invalid. Enter 'local' or 'foreign': ").strip().lower()


    has_visa = False
    if location_type == "foreign":
        has_visa_input = input("Do you have a valid travel visa? (yes/no): ").strip().lower()
        while has_visa_input not in ["yes", "no"]:
            has_visa_input = input("Invalid. Enter 'yes' or 'no': ").strip().lower()
        has_visa = has_visa_input == "yes"


    while True:
        try:
            budget = int(input("What is your maximum budget per person in INR? (e.g., 40000): ").strip())
            if budget > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    valid_group_types = ["solo", "family", "friends", "partner", "senior"]
    while True:
        group_type = input("Who are you travelling with? (solo/family/friends/partner/senior): ").strip().lower()
        if group_type in valid_group_types:
            break
        else:
            print(f"Invalid group type. Please choose from: {', '.join(valid_group_types)}")

    valid_purposes = ["adventure", "relaxation", "culture", "luxury", "nature", "beach"]
    while True:
        purpose = input("What is the main purpose of your travel? (adventure/relaxation/culture/luxury/nature/beach): ").strip().lower()
        if purpose in valid_purposes:
            break
        else:
            print(f"Invalid purpose. Please choose from: {', '.join(valid_purposes)}")

    valid_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    while True:
        month = input("Preferred month of travel? (e.g., December): ").strip().capitalize()
        if month in valid_months:
            break
        else:
            print(f"Invalid month. Please enter a valid month like 'March' or 'October'.")


    return {
        "location_type": location_type,
        "has_visa": has_visa,
        "budget": budget,
        "group_type": group_type,
        "purpose": purpose,
        "month": month
    }
