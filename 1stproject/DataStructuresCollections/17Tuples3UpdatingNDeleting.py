# Collection problems
# Tuples 3
# Editing Tuples

# Tuples are immutable, so we can not add or remove elements
# Although, we can convert the tuple to list, make changes, and convert
# back to tuple using list() and then tuple() functions.
# This will create a different object though with same name but different id()

country = ("Spain", "Italy", "India", "Germany", "France", "Portugal")
print(id(country))
country_temp = list(country)
country_temp.append("Japan")
country_temp.append("USA")
country = tuple(country_temp)
print(country)
print(id(country))
print()

# We can add another tuple and have combined elements; elements will be appended.
# Again, another tuple is created with the same name but different id()
tup2 = ("Brazil", "Australia", "Canada", "United Kingdom", "South Korea")
country = country + tup2
print(country)
print(id(country))
print()

# To remove elements from a tuple, we need to convert into list and back again to tuple.
# Again, another tuple is created with the same name but different id()
country_temp = list(country)
country_temp.remove("Brazil")
country = tuple(country_temp)
print(country)
print(id(country))
