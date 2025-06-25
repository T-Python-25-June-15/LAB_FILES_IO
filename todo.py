from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def readfile():
    file = open("todo.txt",'r',encoding='utf-8')
    return file.read()

def writefile(title):
    file = open("todo.txt",'a+',encoding='utf-8')
    file.write(title + '\n')

while True:
    try:
        question = input("do you want to add a new To-DO item y for yes, n for no? ")

        if question == 'y':
            title = input("Enter the title\n: ")
            towrite = f'{title} - {date} - Not Done'
            writefile(towrite)

        elif question == 'n':
            question2 = input("do you want to list your To-Do items y for yes, n for no?  ? ")

            if question2 == 'y':
                print('\n',readfile())
                
            elif question2 == 'n':
                pass

            elif question2 == 'exit':
                print("thank you for using the To-Do program, come back again soon")
                break

            else:
                print("Wrong Input! ")

        elif question == 'exit':
            print("thank you for using the To-Do program, come back again soon")
            break

        else:
            print("Wrong Input! ")
    except Exception as ex:
        print(f"Type of Error: {ex}")
