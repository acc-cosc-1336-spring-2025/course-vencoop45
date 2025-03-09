#
import decisions

options = int(input("Enter here the amount of options:"))

total = int(input("Enter here the total:"))

result = decisions.get_options_ratio(options, total)

faculty_rating = decisions.get_faculty_rating(result)
print("Faculty Rating", faculty_rating)