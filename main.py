def addNote():
    try:
        user_note = input("write your note: ")
        with open("to_do.txt", 'a', encoding='UTF-8') as my_pen:
            my_pen.write(user_note)
            my_pen.write("\n")
    except:
        print("Error.")
    else:
        print("your note added sucesffuly")

def printAllNotes():
    try:
        with open("to_do.txt", 'r', encoding='UTF-8') as reader:
            lines = reader.readlines()
            print("\n" + "-"* 100 + "\n")
            for note in lines:
                print(note)
            print("-"* 100 + "\n")
    except:
        print("Error")
while True:
    try:
        user_input = input("do you want to add a new TO-DO item? (y or n): ")
        user_input = user_input.lower()
        if user_input == 'exit': break
        if len(user_input) != 1 or user_input != 'y' and user_input != 'n':
            raise ValueError("Invalid input, please try again")
        
        if user_input == 'y':
            addNote()
        
        if user_input == 'n':
            user_input = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no.")
            if user_input == 'exit': break
            if user_input != 'y' and user_input != 'n':
                raise ValueError("Invalid input, please try again")
            else:
                if user_input == 'y':
                    printAllNotes()
        
    except Exception as e:
        print(e)
    
    
