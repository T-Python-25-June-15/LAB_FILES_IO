from datetime import datetime
import json
to_do_list = []
try:
    with open("to_do.json","r",encoding="UTF-8") as file:
        content = file.read()
        to_do_list = json.loads(content)
except Exception as e:
    pass

while True:
        user_choice = input("1)add a item in the To-Do \n 2)display the To-do list \n 3)mark a item in the to-do list \n 4)Search for a item in the to-do list \n Type exit to leave: ")
        if user_choice == "exit":
            print("thank you for using the To-Do program, come back again soon")
            with open("to_do.json","w",encoding="UTF-8") as file:
                content = json.dumps(to_do_list)
                file.write(content)
                file.close()
            break
        if user_choice == "1":
            print()
            print('-'*15)
            user_to_do_list = input("Please enter your To-Do list: ")
            to_do_item = {"title":user_to_do_list,"Date":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Done":False}
            to_do_list.append(to_do_item)
            print("it been added!")
            print("-"*15)
        elif user_choice == "2":
            print()
            print('-'*15)
            for index ,item in enumerate(to_do_list, start=1):    
                print(f"{index} - {item['title']} date : {item['Date']} - {item['Done']}")
            print("-"*15)
        elif user_choice == "3":
            print()
            print('-'*15)
            for index ,item in enumerate(to_do_list, start=1):    
                print(f"{index} - {item['title']} date : {item['Date']} - {item['Done']}")
                user_answer = input("Do you want to mark this one ? if yes press 'y' if no press 'n': ")
                if user_answer.lower() == "y":
                    to_do_list[index-1]['Done'] = True
                else:
                    continue
            print("-"*15)
        elif user_choice == "4":
            print()
            print('-'*15)
            user_search = input("Please enter the title that you are searching for: ")
            result_of_search = [item for item in to_do_list if user_search.lower() in item["title"].lower()]
            print(f"The count of the search result is {len(result_of_search)}")
            print("-"*15)
        else:
            print()
            print('-'*15)
            print("You need to Type a number from 1 to 4 and if you want to leave type 'exit' ")
            print("-"*15)