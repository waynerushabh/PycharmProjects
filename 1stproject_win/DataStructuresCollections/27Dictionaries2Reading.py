# Collection problems
# Dictionaries 2
# Reading Dictionaries

# No Indexing or Slicing as values are in key:value pairs

# Method 1 : Key -> dict-name[key], error if key doesn't exist
scores = {'rohit': 100, 'virat': 40, 'rahul': 80}
print("All scores ->", scores)
print("Rohit :", scores['rohit'])
print("Virat :", scores['virat'])
print("Rahul :", scores['rahul'])
print()

# Method 2 : Iterator
sales = {2000: 450000, 2001: 560000, 2002: 870000}
i = iter(sales)
for year in i:
    print(year, sales[year])
print()

# Method 3 : For loop
for year in sales:
    print(year, sales[year])
print()

# Method 4 : .Get(key [, default]) method of dictionary
# returns value for key if key is in dict, else default.
# If no default defined, then default is None.
# This is no 'KeyError' method
dict1 = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
value1 = dict1.get(1)
value2 = dict1.get(5)
print(value1, value2)
value3 = dict1.get(10)                          # default not defined
print(value3)
value4 = dict1.get(20, "Doesn't exist")         # default defined
print(value4)
print()

# Method 5 : 'View objects' of dictionary using .keys(), .values(), .items()
courses = {'Python': 4000, 'Java': 2000, 'C++': 1500, 'Oracle': 1000}
print(courses)
course_names = courses.keys()
print(course_names)
for i in course_names:
    print(i)
course_list = list(course_names)
print("Course names in List form->", course_list)
print()
course_fees = courses.values()
print(course_fees)
for fees in course_fees:
    print(fees)
fees_list = list(course_fees)
print("Course fees in List form->", fees_list)
print()
course_items = courses.items()
print(course_items)
for item in course_items:
    print(item)
try_list = list(course_items)
print("Courses in List Form->", try_list)
print()
