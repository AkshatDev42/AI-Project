from destination_list import destinations
from user_input import get_user_input
from report_generator import generate_reports
from report_utils import get_best_reports
from report_utils import display_report_to_user
from user_weights_input import get_weight_preferences
from console_ui import show_header, show_footer
from destination_utils import show_all_destinations, compare_destinations, get_suggestions_month, get_suggestions_budget

def main():
    show_header()

    while True:
        print()
        print()
        print("📌 Main Menu")
        print("1. Plan a Destination")
        print("2. Get Suggestions Based on Month")
        print("3. Get Suggestions Based on Budget")
        print("4. Compare Destinations")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            weights = get_weight_preferences()
            user = get_user_input()
            reports = generate_reports(user, destinations, weights)
            top_reports = get_best_reports(reports)
            display_report_to_user(top_reports)

        elif choice == "2":
            valid_months = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]

            month = None
            while True:
                month = input("Enter the month you want to travel (e.g., December): ").strip().capitalize()
                if month in valid_months:
                    break
                else:
                    print("❌ Invalid month. Please enter a valid full month name like 'January'.")

            get_suggestions_month(destinations, month)

        elif choice == "3":
            while True:
                budget_input = input("\nEnter your budget (in ₹): ").strip()
                if not budget_input:
                    print("❌ Budget cannot be empty.")
                    continue

                try:
                    budget = int(budget_input)
                    if budget < 0:
                        print("❌ Budget must be a positive number.")
                        continue
                    get_suggestions_budget(destinations, budget)
                    break  # Exit the loop after valid input
                except ValueError:
                    print("❌ Invalid input. Budget must be a number.")


        elif choice == "4":
            destination_names = show_all_destinations(destinations)

            while True:
                dest1 = input("\nEnter name of first destination: ").strip()
                if not dest1:
                    print("❌ Destination name cannot be empty.")
                elif dest1 not in destination_names:
                    print("❌ Destination not found. Please choose from the list.")
                else:
                    break
            
            while True:
                dest2 = input("Enter name of second destination: ").strip()
                if not dest2:
                    print("❌ Destination name cannot be empty.")
                elif dest2 not in destination_names:
                    print("❌ Destination not found. Please choose from the list.")
                elif dest2 == dest1:
                    print("❌ Please enter a different destination.")
                else:
                    break

            compare_destinations(destinations, dest1, dest2)


        elif choice == "5":
            show_footer()
            break


main()