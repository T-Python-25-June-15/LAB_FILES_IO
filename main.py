



msg = input("\nWelcome ! Do do you want to add a new To-Do item? answer y for yes and n for no.")

while msg != 'exit':
    if msg == 'y':
    
        todo = input("\nenter you To-do item:")
        File = open("LAB_FILES_IO/to_do.txt", "a", encoding='UTF-8')
        File.write(todo + "\n")
        File.close()
        print("To-Do item added successfully!")
        

    elif msg == 'n':
        show = input("\ndo you want to list your To-Do items ? answer y for yes and n for no.")
        if show == 'y':
            File = open("LAB_FILES_IO/to_do.txt", "r", encoding='UTF-8')
            File.seek(0)
            print(File.read())
            File.close()
        else:
            continue
    
    else:
        print("Invalid input")
        continue

    msg = input("\ndo you want to add a new To-Do item? answer y for yes and n for no.")


