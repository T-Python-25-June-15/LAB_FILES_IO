#Luluh Almogbil 
'''
# LAB_FILES_IO


## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . 
Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , 
then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''

while True:
    choice = input("Do you want to ADD a new To-Do item? (y/n). Type 'exit' to exit the program: ")
    if choice.lower() == "y":#write/append in my list
        addItem = input("Enter your To-Do item:")
        file = open("to_do.txt","a+",encoding="utf-8")#1-open file
        content = file.write(addItem + "\n")#2-do operation(write/append)
        file.close()#3-close file  
        print("Added Successfuly!")
        
    elif choice.lower() == "n":#read my list
        choice2 = input("Do you want to LIST your To-Do items ? (y/n). Type 'exit' to exit the program: ")
        if choice2.lower() == "y":#list items
            with open("to_do.txt","r") as file:
                content = file.readlines()
                if not content:#the file is empty
                    print("Empty File ..")
                    file.close()
                else:
                    print("Your To-Do List: ")
                    for i in range(len(content)):
                        print(f"{i+1}- {content[i].strip()} ") #.strip to remove the \n
                
                    #file.close() NO NEED FOR CLOSE WHEN USING WITH
                             
        else:# if no
            continue # return to the first question
    else :# if user types exit
        break   
    