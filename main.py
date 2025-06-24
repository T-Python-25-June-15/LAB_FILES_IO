#Lab files io (wasan alqahtani)
try:
    while True:
        print("-"*20)
        answer = input("do you want to add a new To-Do item? 'y' for yes and 'n' for no: \n").lower()

        with open("to_do.txt", "a+", encoding="UTF-8") as file:
            if answer == "y":
                To_Do = input("please write your to do list: \n")
                file.write(To_Do + "\n")

            elif answer == "n":
                print("-"*20)
                option = input("do you want to list your To-Do items ? 'y' for yes and 'n' for no: \n").lower()
                print("-"*20)
                
                if option == "y":
                    file.seek(0)
                    print("Your to Do list are:")
                    print(file.read())
                else:
                    continue 
            elif answer == "exit": 
                    print("thank you for using the To-Do program, come back again soon")
                    break
            else:
                print("Wrong entry try again")         
except Exception as e:
    print(e.__class__)