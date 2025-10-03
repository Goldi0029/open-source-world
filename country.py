
city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")

australia = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]

def get_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")
