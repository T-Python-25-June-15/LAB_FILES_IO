while True:
    user=input(" do you want to add a new To-Do answer by n or y? ")
    if user =="y":
        ask=input("type in new To-Do item: ")
        file=open("to_do.txt","a",encoding="UTF-8")
        file.write(ask+"\n")
        file.close()
    elif user== "n":
        p=input(" do you want to list your To-Do items ? answer y for yes and n for no. ")
        if p== "y":
             try:
                 file=open("to_do.txt","r",encoding="UTF-8")
                 print("here your to do item -- ",file.read())
                 file.close()
             except:
                 print("you dont have any item")
        elif p== "n":
          print("No items to showo")
    elif user=="exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'")