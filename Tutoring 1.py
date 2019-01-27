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

#Insertion
#Start a loop to insert the whole class. 
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

#Show the remaining students list.
show()

#Deletion
#Prompt if the user wants to delete the users that left.
delete = str(input("Do you wish to delete a student from the list? (y/n) : ")).lower()
while (delete=="y"): #While user wants to delete
    toremove = input("Who do you wish to delete from the list? (name) : ")
    remove(toremove) #call the function declared on top.
    delete = str(input("Do you wish to delete another student from the list? (y/n) : ")).lower()


#Show again the remaining table.
show()



#2d Array.
#The idea behind this is to create an array with the data you need, and store it
#inside another array. So, when you access an index of students, you actually access
#another array that contains one specific student's info. Then, accessing that
#array in indexes 0..3 gives you the student's info field you desire.

#Example:
name = input("Student name: ")
email = input("Email address: ")
dob = input("Date of birth: ")
std_id = input("Student ID: ")

#Create the student info array
student_info = [name, email, dob, std_id]
#add it to the students list.
students.insert(len(students), student_info)

















