# To-Do List app
while True:
    user_input = input('do you want to add a new To-Do item? (y, n, exit): ')
    if user_input == 'y':
        print('now we write insid file ...')
        with open('to_do.txt', 'a+', encoding='UTF-8') as file:
            user_todo = input('please type your new todo: ')
            file.write(user_todo + '\n')

    elif user_input == 'n':
        user_list_todo = input('do you want to list your To-Do items? (y, n) ')
        if user_list_todo == 'y':
            with open('to_do.txt', 'r', encoding='UTF-8') as file:
                todo_list = file.readlines()
                for i, line in enumerate(todo_list):
                    print(f'{i}. {line}')

    elif user_input == 'exit':
        break
print('thank you for using the To-Do program, come back again soon')