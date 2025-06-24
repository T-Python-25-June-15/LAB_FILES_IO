while True:
    try:
        user_element_choice = input("do you want to add a new To-Do item (y/n) or (exit) to quit? ")
        if user_element_choice.lower() == "y":
            user_element_input = input("Please write the new To-Do item: ")
            with open("to_do.txt","a+",encoding="UTF-8") as file:
                file.write(f"{user_element_input}\n")
        elif user_element_choice.lower() == "n":
            user_list_input = input("Do you want to list your To-Do items (y/n) or (exit) to quit?: ")
            if user_list_input.lower() =="y":
                with open("to_do.txt","r",encoding="UTF-8") as file:
                    print(file.read())
            elif user_list_input.lower() == "exit":
                break
            elif user_list_input.lower() =="n":
                continue
            else:
                print("Invalid input!") 
        elif user_element_choice.lower() == "exit":
            break
        else:
            print("Please write (y/n) or exit only.")
    except:
        print("An error occurred!") 