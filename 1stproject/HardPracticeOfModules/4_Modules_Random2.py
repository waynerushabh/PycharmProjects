# Generating Random Data of names with corresponding info

import random

first_names = ['Ajay', 'Amar', 'Amit', 'Akash', 'Abhishek', 'Avirup', 'Avinash', 'Ajit', 'Akshay', 'Ashutosh', 'Arun',
               'Amrit', 'Abhay', 'Ram', 'Shyam', 'Vijay', 'Manoj', 'Sourav', 'Sachin']

last_names = ['Sharma', 'Mishra', 'Singh', 'Gupta', 'Verma', 'Kumar', 'Yadav', 'Anand']

cities = ['Rampur', 'Akbarbad', 'Amirbad', 'Salmanbad', 'Shahrukhbad', 'Premnagar', 'Nizamabad', 'Nawabnagar']

states = ['Vidarbha', 'Coorg', 'Bundelkhand', 'Mewar', 'Marwar', 'Hadaut', 'UpperAssam']

# special_chars = list("!#$%&'*+-/=?^_`{|}~.")
# print(special_chars)
# We can possibly use these symbols in emails as well, although only . and _ are commonly used.

emails = ['gmail', 'hotmail', 'yahoo', 'mail', 'protonmail']

domains = ['com', 'edu', 'gov', 'co.in', 'org', 'io', 'ai']

for num in range(20):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    mobile = f'{random.randint(700, 999)}{random.randint(1000000, 9999999)}'

    email = first_name.lower() + random.choice(["_", "."]) + last_name.lower() + '@' + random.choice(
        emails) + "." + random.choice(domains)

    city = random.choice(cities)
    state = random.choice(states)

    print(f'{first_name} {last_name}\n{mobile}\n{email}\n{city}, {state}\n')