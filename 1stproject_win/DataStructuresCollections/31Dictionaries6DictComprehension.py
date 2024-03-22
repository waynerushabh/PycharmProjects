# Collection problems
# Dictionaries 6
# Dictionary Comprehensions

# Syntax 1 - {key: value for variable in iterable}

print()
dict1 = {}
for num in range(1, 11):                    # without comprehension
    dict1[num] = num**2
print(dict1)
print()
dict2 = {num: num**2 for num in range(1, 11)}
print(dict2)
print()

# wap to create dictionary of n years sales
print()
n = int(input("Enter no. of years = "))
sales = {int(input("year = ")): int(input("sales = ")) for i in range(n)}
print(sales)

# Syntax 2 - {key: value for variable in iterable if condition}
# Example 1 -
print()
grade_dict = {'naresh': 'A', 'suresh': 'B', 'kishore': 'C', 'ramesh': 'A', 'rajesh': 'B', 'raman': 'A'}
print(grade_dict)
print()
grade_dict_a = {name: grade for name, grade in grade_dict.items() if grade == 'A'}
grade_dict_b = {name: grade for name, grade in grade_dict.items() if grade == 'B'}
grade_dict_c = {name: grade for name, grade in grade_dict.items() if grade == 'C'}
print(grade_dict_a)
print(grade_dict_b)
print(grade_dict_c)
print()

# Example 2 -
print()
sales_data = {2000: 45000, 2001: 55000, 2002: 35000, 2003: 25000, 2004: 65000, 2005: 20000, 2006: 15000}
print(sales_data)
print()
sales_above_50k = {year: sales for year, sales in sales_data.items() if sales >= 50000}
sales_below_50k = {year: sales for year, sales in sales_data.items() if sales <= 50000}
print(sales_above_50k)
print(sales_below_50k)
print()

# Syntax 3 - {key: value for variable in iterable for in iterable if test}
