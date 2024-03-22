# Collection problems
# LISTS 10
# All Queues Implementations using List operations
# Queues are FIFO - First In First Out, i.e. First item inserted is removed first
# 2 main operations - del queue[0] (to remove items out) and append() ( to add items in)

# Complete Queue Operations - 1. Add, 2. Remove, 3. Display, 4. Exit

# wap to implement Queue Data Structure

import time
queue = []
while True:
    time.sleep(1.2)
    print("*** Queue Operations ***")
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Exit")
    print()

    opt = int(input("Enter any option = "))
    print()

    if opt == 1:
        ele = int(input("Enter element = "))
        queue.append(ele)
        print()
        print(f'{ele} added to queue successfully.')
        print()
        print(queue)
        print()
    elif opt == 2:
        if len(queue) == 0:
            print("Error : Queue is empty. \nLesson of the Day -> Add some values to remove some values.")
            print()
            print(queue)
            print()
        else:
            ele = queue[0]
            del queue[0]
            print(f'{ele} removed from queue successfully.')
            print()
            print(queue)
            print()
    elif opt == 3:
        if len(queue) == 0:
            print("Error : Queue is empty. \nLesson of the Day -> Add some values to display the queue.")
            print()
            print(queue)
            print()
        else:
            print()
            print(queue)
            print()
    elif opt == 4:
        print()
        print("Quitting ... ")
        print()
        break
    else:
        print("Error : Wrong operation selected.\nSelect the correct operation from the Queue Operations menu again.")
        print()
