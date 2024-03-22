# All functions under Random Module

import random


print("Float Practice -")
fl_num = random.random()
fl_range = random.uniform(1, 10)
print(fl_num)
print(fl_range)
print()

print("Integer Practice -")
int_num = random.randint(1, 6)
print("Dice number", int_num)
int_num1 = random.randint(0, 1)
if int_num1== 1:
    print("Heads!")
else:
    print("Tails!")
print()

print("Choice -")
baby_names = ['Lanesra/Lana', "Lavanya/Lina", "Lorena", "Loredana", "Mayur", "Mayukh", "Mayuresh", "Reel"]
selected_name = random.choice(baby_names)
print("Selected Name - {}".format(selected_name))
print()
print("Choices - ")
random_names = random.choices(baby_names, weights=[5, 5, 1, 1, 3, 1, 3, 3], k=3)
print("Possible Selected Names = ", random_names)
print()
print("All baby names - ", baby_names)
print()

deck = list(range(1, 53))
print("All cards in sequence ->", deck)
random.shuffle(deck)
print("Cards Shuffled ->", deck)
print()
print("Sample -")
deal = random.sample(deck, k=4)
print("Your Cards =", deal)

# trying seek()

print("Trying seek() ->")

abc = random.seed()

print(abc)