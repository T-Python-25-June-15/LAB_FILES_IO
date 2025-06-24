while True:
    user_input = input("Do you want to add a new To-Do item? (y/n or exit): ").lower()

    if user_input == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    elif user_input == "y":
        new_item = input("Enter your new To-Do item: ")
        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write(new_item + "\n")

    elif user_input == "n":
        read_input = input("Do you want to list your To-Do items? (y/n): ").lower()
        if read_input == "y":
            try:
                with open("to_do.txt", "r", encoding="utf-8") as file:
                    print("\nYour To-Do List:")
                    for line in file:
                        print("- " + line.strip())
            except FileNotFoundError:
                print("No To-Do list found yet.")
        elif read_input == "n":
            continue
        else:
            print("Please enter 'y' or 'n'.")

    else:
        print("Please enter 'y', 'n', or 'exit'.")
