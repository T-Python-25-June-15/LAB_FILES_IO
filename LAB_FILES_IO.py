# Do-List


filename = "do_list.txt"

while True:
    user = input("Do you want to add a new To-Do item? Y or N: ").lower()

    if user == "y":
        user_item = input("Enter your To-Do item: ")
        file = open(filename, "a", encoding="utf-8")
        file.write(user_item + "\n")
        print("Item added.")

    elif user == "n":
        file=open(filename, "r", encoding="utf-8")
        print("\nYour current To-Do list:")
        print(file.read())
        
        exit_choice = input("Do you want to exit the program? Y or N: ").lower()
        if exit_choice == "y":
            print("Thank you for using the To-Do program, come back again soon!")
            break

    else:
        print("Invalid input. Please enter Y or N.")
