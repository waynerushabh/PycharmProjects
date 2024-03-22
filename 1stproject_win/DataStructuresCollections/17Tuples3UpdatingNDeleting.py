# Collection problems
# Tuples 3
# Editing Tuples

# Tuples are immutable, so we can not add or remove elements
# Although, we can convert the tuple to list, make changes, and convert
# back to tuple using list() and then tuple() functions.

country = ("Spain", "Italy", "India", "Germany", "France", "Portugal")
country_temp = list(country)
country_temp.append("Japan")
country_temp.append("USA")
country = tuple(country_temp)
print(country)

tup2 = ("Brazil", "Australia", "Canada", "United Kingdom", "South Korea")
country = country + tup2
print(country)
country_temp = list(country)
country_temp.remove("Brazil")
country = tuple(country_temp)
print(country)
