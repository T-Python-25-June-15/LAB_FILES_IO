file = open("to_do.txt" , "a+" , encoding="UTF-8")
file.seek(0)

while True:
   user_answer = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no to exit write 'exit'. \n")
   if user_answer == "y" :

      note = input("type your new to do item : \n")
      file.writelines(note + "\n")
      

   elif user_answer == "n" :
  
    answer = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no.")
    if answer == "y":
       with open("to_do.txt", "r", encoding="utf-8") as file:
         file.seek(0)
         lines = file.readlines()
         for line in lines:
             print(line.strip())

       

   elif user_answer == "exit" :
     print("thank you for using the To-Do program, come back again soon")
     break

file.close()