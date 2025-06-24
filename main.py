


    




def main():
    print("-"*35 + "Welcome To TO_Do List Program" + "-"*35 + '\n')
    choice = input("Do you want to add a new To-Do item? (answer by y for yes and n for no), or exit: ")
    while choice != 'exit':
        match choice:
            case 'y':
                item = input("Type your new To-Do item: ")
                with open('To-Do.txt','a', encoding='UTF-8') as file:
                    file.write(item + '\n')

            case 'n':
                option = input("Do you wnat to list your To-Do items? (answer by y for yes and n for no): ")
                if option == 'y':
                    with open('To-Do.txt','r', encoding='UTF-8') as file:
                        items = file.read()
                        print(items)

                elif option == 'n':
                    break
                else:
                    print("invalid answer please try again")

            case 'exit':
                break
            case _:
                print("invalid answer please try again")

        choice = input("Do you want to add a new To-Do item? (answer by y for yes and n for no), or exit: ")

    print("Thank you for using the To-Do program, come back again soon")

main()
