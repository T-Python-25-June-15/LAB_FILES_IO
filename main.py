
toDoList = open("to_do.txt", "a+", encoding="utf-8")




while True:
    print("-"*30)
    user_answers = input("Wellcome\nDo you want to add a new To-Do item? \nAnswer by \"y\" for yes and \"n\" for no or \"exit\" to exit the progeram:")

    if user_answers =="y":
            while True:
                print("Enter your new To-Do item Enter or \"exit\" to exit:")
                user_toDoLlist= input()
                if user_toDoLlist == "exit": 
                    break
                else:
                    toDoList.write(user_toDoLlist + "\n")



    elif user_answers=="n":
        user_answers= input("Do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no: ")
        while True:
            if user_answers=="y":
                print("Your to Do itemes are:")
                toDoList.seek(0)
                print(toDoList.read())
                break
            else: 
                break


    elif user_answers =="exit":
         break
    else: print("Please, Answer by \"y\" for yes and \"n\" for no or \"exit\" to exit the progeram: ")
    


print("thank you for using the To-Do program, come back again soon")
toDoList.close()


