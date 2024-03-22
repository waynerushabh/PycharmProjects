# Collection problems
# LISTS 9
# All Stacks Implementations using List operations
# Stacks are LIFO - Last In First Out, i.e. Last item inserted is removed first
# 2 main operations - pop() (to pop/remove items out) and append() ( to push items in)

# Complete Stack Operations - 1. Push, 2. Pop, 3. View, 4. Exit

# wap to implement Stack Data Structure

import time
stack = []                                              # Empty list called stack
while True:
    time.sleep(1.2)
    print("*** Stack Operations ***")                   # Options Menu display
    print("1. Push")
    print("2. Pop")
    print("3. View")
    print("4. Exit")
    print()

    opt = int(input("Enter any option = "))             # Option selected by user
    print()

    if opt == 1:                                        # Push operation
        ele = int(input("Enter element = "))
        stack.append(ele)
        print()
        print(f'{ele} pushed inside stack successfully.')
        print()
        print(stack)
        print()
    elif opt == 2:                                      # Pop operation
        if len(stack) == 0:                             # Checking for empty stack, brings back to menu is empty
            print("Error : Stack is empty. \nLesson of the Day -> Push some values to pop some values.")
            print()
            print(stack)
            print()
        else:
            ele = stack.pop()                           # Popping if not empty stack
            print(f'{ele} popped from stack successfully.')
            print()
            print(stack)
            print()
    elif opt == 3:                                      # View operation
        if len(stack) == 0:                             # Checking for empty stack, brings back to menu is empty
            print("Error : Stack is empty. \nLesson of the Day -> Push some values to view some values.")
            print()
            print(stack)
            print()
        else:                                           # Viewing if not empty stack
            print()
            print(stack)
            print()
    elif opt == 4:                                      # Exit operation, breaks the loop
        print()
        print("Quitting ... ")
        print()
        break
    else:                                               # Wrong number input, brings back the menu
        print("Error : Wrong operation selected.\nSelect the correct operation from the Stack Operations menu again.")
        print()
