from datetime import datetime
import json

to_do_list = []


try:
    with open('to_do_list.json', 'r', encoding="UTF-8") as file:
        to_do_list = json.load(file)
except:
    to_do_list = []  

user_menu = '''
1- add to do list.
2- show your to do list.
3- search your to do list.
4- exit
'''

while True:
    user_choice = input(user_menu)

    if user_choice == "1":
        title = input("What you want to add?")
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        to_do_item = {
            "title": title,
            "created_at": created_at,
            "is_done": False
        }
        to_do_list.append(to_do_item)
        print("Added")

    elif user_choice == "2":
        for index, item in enumerate(to_do_list, start=1):
            print(f"{index}- {item['title']} - {item['created_at']} - {'Done' if item['is_done'] else 'Not Done'}")
            is_done_input = input("Is this done? (y/n): ")
            if is_done_input == "y":
                to_do_list[index - 1]["is_done"] = True

    elif user_choice == "3":
        search = input("Search for: ")
        found_results = [item for item in to_do_list if search.lower() in item['title'].lower()]
        print(f"Found {len(found_results)} result(s):")
        for item in found_results:
            print(f"- {item['title']}")

    elif user_choice == "4":
        print("Saving and exiting. Goodbye!")
        with open("to_do_list.json", "w", encoding="utf-8") as file:
            json.dump(to_do_list, file, indent=2)
        break

    else:
        print("Please choose a valid option.")