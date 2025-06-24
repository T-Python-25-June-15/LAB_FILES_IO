#bonus wasan alqahtani
from datetime import datetime
import json 

ToDo_list:list = []
to_do = {}
try:
    with open("ToDo.json", "r", encoding= "UTF-8") as file:
        content = file.read()
        ToDo_list = json.loads(content)
        while True:
            print("Welcome to To-Do list Program")
            print("-"*20)
            print("1. Add new To Do ")
            print("2. Display")
            print("3. Search for spesific title")
            print("4. Done something in the to-do list")
            print("5. Exit")

            option= input("please enter a number from menue above: ")
            match option:

                case "1":
                    print("Add new To-do ")
                    print("-"*20)
                    title = input("Enter Title (what you want to do): ")
                    time_ofcreation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    to_do = {
                    'title' : title,
                    'creation_date' : time_ofcreation,
                    'done' : False
                    }
                    ToDo_list.append(to_do)
                    print("Added successfully")
                 
            

                case "2":
                    for (num, item) in enumerate(ToDo_list, start=1):
                        finish:str = ""
                        if item['done']:
                           finish = "Done"
                        else:
                            finish = "Not Done"
                    
                        print(f"{num}- {item['title']} - {item['creation_date']} - {finish}")
        
                case "3":
                   
                    search = input("what you want to search for: ")
                    result = [title for title in ToDo_list if search.lower() in title['title'].lower()]
                    print(f"Number of found results in searching: {len(result)}")
                    for num, item in enumerate(result, start=1):
                        print(f"{num} - {item['title']}")       
                   
                 
                  
                case "4":
                   
                     for num, item in enumerate(ToDo_list, start=1):
                        finish:str = ""
                        if item['done']:
                           finish = "Done"
                        else:
                            finish = "Not Done"
                        print(f"{num}- {item['title']} - {item['creation_date']} - {finish}")
                        done_input = input("Do you done this?: 'y' for yes and 'n' for no")
                        if done_input == "y":
                             ToDo_list[num-1]["done"] = True
                  
                    

                case "5":
                    print("All your to do list have been added to file")
                    print("thank you for using this program")
                    
                    with open("ToDo.json", "w" ,encoding= "UTF-8") as file:
                       content = json.dumps(ToDo_list)
                       file.write(content)
                       break
                case _:
            
                    print("invalid number try again")

except Exception as e:
    print(e.__class__)

   