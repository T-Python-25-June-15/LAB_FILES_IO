
# loop to the program running until the user chooses to exit
while True :
    # Ask the user
    user_input=input("do you want to add a new To-Do item 'y' for yes and 'n' for no.?")

    if user_input == "y":
        file = open("to_do.txt","a+",encoding="UTF-8")
        input2 = input("Type your To-Do item:")
        # Open the file & write
        file.write(input2 + "\n")
        file.close()

    elif user_input == "n":
       input3=input("do you want to list your To-Do items ?")

       if input3 == "y":
           # Open the file & display the contents
           file = open("to_do.txt","r",encoding="UTF-8")
           file.seek(0)
           content = file.read()
           print("Your To-DO:")
           print(content)
           file.close()
       else:
           continue
    # end the program
    elif user_input == "exit":
        print("thank you for using the To-Do program, come back again soon")  
        break
