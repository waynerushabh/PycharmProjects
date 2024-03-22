# Collection problems
# SETS 7
# Frozen Sets

# Nested sets - Sets cannot contain sets inside cause sets are hashable,
# and sets cannot have unhashable elements.
# But sets can contain frozen sets , which are hashable/immutable.
# It is a set which can not be altered after creation.
# It can be used as a dictionary key or as an element of another set.


# Creating frozen set objects - using frozenset([iterable])

try:
    # set1 = {{1, 2}, {4, 5}}
    print()
    f_set1 = frozenset
    print(f_set1)
    # f_set1.add(10)
    f_set2 = frozenset(range(10, 101, 10))
    print(f_set2)
    f_set3 = frozenset({100, 70, 40, 10, 80, 50, 20, 90, 60, 30})
    # f_set3.remove(10)
    # f_set4 = frozenset(set1)
    # print(f_set4)
except TypeError:
    print("Sets can not be elements of a set. Inner Sets need to be Frozen.")
except AttributeError:
    print("We can not add or remove elements to a Frozenset.")
else:
    print("Some successful operations.")
finally:
    print("This was to learn differences and properties of Frozen Sets vs Sets.")
