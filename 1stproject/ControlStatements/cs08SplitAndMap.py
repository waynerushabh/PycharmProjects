#simple if elif else problems
#Using Split and Map functions
#Girl Names like Lanesra, Lavanya, Lorena, Loredana, Lipika etc.
#improve with L letter check later on

girl_names=input("Input 3 good first names for a baby girl, separated by spaces = ")
collected_names = girl_names.split(" ")

print(girl_names)
print(collected_names)

x,y,z = map(str,collected_names)
print(x,y,z)
print(type(x))

#first_letter = x.split("L")
#a = map(str,first_letter)
#print(a)
#if a!='L' or a!='l':
    #print("Suggest names starting with L please. Thanks!")