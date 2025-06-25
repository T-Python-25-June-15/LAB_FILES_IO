

menu = '''Do you want to add a new To-Do item?
1. for yes (y).
2. for no (n).
3. for exit (exit).
'''

while True:
    print("-" * 34)
    print("Welcome to our to-do-list program.")
    print("-" * 34)

    option = input(menu).lower().strip()

    match option:
        case "y":
            print()
            userInput = input("Enter what you want to say: ")
            to_do_item = open("to_do.txt" , "a+" , encoding="UTF-8")
            content = to_do_item.write(userInput + "\n")
            to_do_item.close()
            print()
            print("The item added successfully.")

        case "n": 
            menu2 = '''do you want to list your TO-Do items?
            1. for yes (y).
            2. for no (n).
            '''
            while True:
                print()
                option2 = input(menu2).lower().strip()
                match option2:
                    case 'y':
                        print()
                        to_do_item2 = open("to_do.txt" , "r" , encoding="UTF-8")
                        content2 = to_do_item2.read()
                        print(content2)
                        to_do_item2.close()
                    case 'n':
                        print()
                        print("           OK!")
                        print()
                        break
                    case _ :
                        print()
                        print("Invalid inputs, please only enter (y,n).")

        case "exit":
            print()
            print("thank you for using the To-Do program, come back again soon")
            break

        case _ :
            print()
            print("Invalid inputs, please only enter (y,n).")