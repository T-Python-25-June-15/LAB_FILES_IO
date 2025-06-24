counter = 1
while True:
    try:
        user_choice = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no: ")
        if user_choice.lower() == 'exit':
            print("thank you for using the To-Do program, come back again soon")
            break
        if user_choice.lower() == 'y':
            user_to_do_list = input("Please enter your To-Do list: ")
            file = open("to_do.txt", "+a", encoding="utf-8")
            file.write(f"{counter}) {user_to_do_list} \n")
            counter += 1
            file.close()
        elif user_choice.lower() == 'n':
            user_to_do_list_show = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no: ")
            if user_to_do_list_show.lower() == 'y':
                file = open("to_do.txt", "r", encoding="utf-8")
                file.seek(0)
                content = file.read()
                print(content)
                file.close()
            #I added this part: since he don't want to show his to-do list or even add so maybe he wanted to leave
            else:
                break
        else:
            print("you can only choose 'y' or 'n' and 'exit' to leave ")
            user_choice = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no: ")
    except:
        print("There is an error")            