#Age_calculator

age = int(input("Enter your age:"))

years = age
months = years * 12
weeks = months * 4
hours = weeks * 7 * 24
seconds = hours * 60

print(f"Your age in year = {years}")
print(f"Your age in months = {months}")
print(f"Your age in weeks = {weeks}")
print(f"Your age in hours = {hours}")
print(f"Your age in seconds= {seconds}")