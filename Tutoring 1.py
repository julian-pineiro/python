students = [] #Create the Array
keep_inserting = True

#Define a function to show the students table. If you don't
#know what functions are yet, just copy the text inside and
#replace it where it says "show()" in the last line.
def show():
    print("Showing the list of students:")
    for i in range(len(students)):
        print(str(i+1)+"- "+students[i]+"\n")

#deletes a student from the list.
def remove(name):
    print("Deleting "+name+" from the list of students...\n")
    for i in range(len(students)-1):
        if (name in students[i]):
            del students[i]
            print("Successfully deleted!\n")




    
while (keep_inserting==True):
    name = input("Student Name: ") #Input the name
    email = input("Student Email: ") #Input the email

    #Now that we've got email and name we can concatenate them.
    #We can use the "+" operator between strings to concatenate.
    #Remember we must add a "#" in between.
    element = name+"#"+email

    #Write the String to the next array element
    #To do this, we ask "students" how many elements it contains,
    #And then we insert in that same index as follows:

    #students[len(students)] = element
    students.insert(len(students), element)

    #Uncomment this to see what you just inserted.
    #print("You inserted "+students[len(students)])
    

    ans = input("Do you want to insert another student? y/n : ")
    ans.lower()
    if (ans=="n"):
        keep_inserting = False

show()

delete = str(input("Do you wish to delete a student from the list? (y/n) : ")).lower()
while (delete=="y"):
    toremove = input("Who do you wish to delete from the list? (name) : ")
    remove(toremove)
    delete = str(input("Do you wish to delete another student from the list? (y/n) : ")).lower()
    show()


