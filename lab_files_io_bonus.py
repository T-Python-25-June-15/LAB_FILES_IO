from datetime import datetime
import json

to_dos:list = []

try:
    with open('to_dos.json', 'r', encoding="UTF-8") as file:
        content = file.read()
        to_dos = json.loads(content) #Decode
except Exception as e:
    pass


usage = '''
1- add to do list.
2- display your to dos.
3- search your to dos.
4- exit
'''
while True:
    
    user_choice:str = input(usage)

    if user_choice == "1":
        title = input("Enter your to do:\n")
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #2025-02-14 05:40:00
        to_do_item = {
            "title" : title,
            "created_at" : created_at,
            "is_done" : False
        }

        to_dos.append(to_do_item)
        print("added!")
        input("")
        
    elif user_choice == "2":
        for index, item in enumerate(to_dos, start=1):

            print(f"{index}- {item['title']} - {item['created_at']} - {'Done' if item['is_done'] else 'Not Done'}")
            is_done_input = input("Is this done ? y for yes, n for no: ")
            if is_done_input == "y":
                to_dos[index-1]["is_done"] = True
            
        input("...press Enter to continue")
    elif user_choice == "3":
        search = input("Search for: ")
        #found_results = [item for item in to_dos if search.lower() in item['title'].lower()]
        found_results = list(filter(lambda item: search in item['title'], to_dos))
        print(f"Found results {len(found_results)}")
        for item in found_results:
            print(f"- {item['title']}")

        
        input("..Press Enter to continue")


    elif user_choice == "4":
        print("Goodbye mate !")
        with open("to_dos.json", "w", encoding="utf-8") as file:
            content = json.dumps(to_dos, indent=2) #Encode
            file.write(content)
        break
    else:
        print("Please choose a valid choice")
