from destination_list import destinations
from user_input import get_user_input
from report_generator import generate_reports
from report_utils import get_best_reports
from report_utils import display_report_to_user
from user_weights_input import get_weight_preferences

user = get_user_input()
weights = get_weight_preferences()
reports = generate_reports(user, destinations, weights)
top_reports = get_best_reports(reports)
display_report_to_user(top_reports)