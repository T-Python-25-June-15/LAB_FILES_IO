print("Welcome to the to do list System")
while True:
    answer:str = input("Do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no or write 'Exit':")
    if answer == "y":
        to_do_item:str = input("Please type your new To-Do item:")
        with open("to_do.txt", "a+" ,encoding="UTF-8") as to_do:
                to_do.write(to_do_item + "\n")
    elif answer == "n":
        answer:str = input("Do you want to list your To-Do items ? answer 'y' for yes and 'n' for no or write 'Exit':")
        if answer == "y":
            with open("to_do.txt", "r" ,encoding="UTF-8") as to_do:
                print(f"Your to-do list are: \n:{to_do.read()}")
        elif answer == "n":
            continue
        else:
            print("Please enter a valid input")
    elif answer == "Exit":
        print("Thank you for using the To-Do program, come back again soon :)")
        break
    else:
        print("Please enter a valid input")