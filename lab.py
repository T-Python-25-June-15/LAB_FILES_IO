while True:
 user_input = input("Do you want to add a new To-Do item? answer: y or n or 'exit' to stop  ")
 if user_input == 'exit' or user_input == 'EXIT':
     print("Thank you for using our ToDo app, goodbye")
     break
 file = open("text1.txt", "a+", encoding="UTF-8")
 if user_input == 'y' or user_input == 'Y':
     while True:
           user_todo_input = input("okay, Enter your ToDo item and type finish to stop: ")
           file.write(user_todo_input + "\n")
           if user_todo_input == 'finish' or user_todo_input == "Finish" or user_todo_input == "FINISH":
               break
    
 elif user_input == 'n' or user_input == 'N':
     user_answer = input("Alright, would you want to list your To-Do items? ")
     if user_answer == 'y' or user_input == 'Y':
         file.seek(0)
         print(f"The to-do list containes: {file.read()}")
    
 else:
     print("Invalid, please enter y or n")

