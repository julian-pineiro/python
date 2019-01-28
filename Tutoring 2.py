#List of data
nameAndEmail = []
#Number of elements in the list?
count = int(input("How many students are there in this class? "))

#Alright, yes. Here we load them.
for i in range(count):
    name = str(input("Student Name: "))
    email = str(input("Student's Email Address: "))
    #newString = name + "#" + email
    #We request the new data
    dob = str(input("Student's date of birth: "))
    std_id = str(input("Student's ID: "))
    newStudent = [name, email, dob, std_id]
    #We change what we append to "newStudent"
    nameAndEmail.append(newStudent)

print()
dash = '-' *50

print('{:^20}{:^30}'.format("STUDENT NAME", "STUDENT EMAIL ADDRESS"))
print(dash)
for i in range(count):
        #now, data is a new list with 4 elements.
        data = nameAndEmail[i]
        #We need to print all four elements of data.
        print('{:^20}{:^30}'.format(data[0], data[1], data[2], data[3]))

def delStudent():
    delStudent = str(input("Do you wish to delete any students? (y/n) "))
    if delStudent == "y":
        print(nameAndEmail)
        print()
        value = int(input("Which value would you like to delete? (Enter a number) "))
        value -= 1
        print()
        print("Updated student data: ")
        del nameAndEmail[value]
        for i in nameAndEmail:
            print(i)
    else:
        return

delStudent()

namePrompt = str(input("Please input a student's name: "))
for i in range(count):
    data = nameAndEmail[i].split('#')
    for name in data:
        if name.find(namePrompt) != -1:
            print(data[1])
