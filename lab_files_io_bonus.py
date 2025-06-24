from datetime import datetime
import json

to_dos: list = []

try:
    with open('to_dos.json', 'r', encoding="UTF-8") as file:
        content = file.read()
        to_dos = json.loads(content)  
except Exception:
    pass


def add_to_do():
    title = input("Enter your to do:\n")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_do_item = {
        "title": title,
        "created_at": created_at,
        "is_done": False
    }
    to_dos.append(to_do_item)
    print("Added!")
    input("Press Enter to continue...")


def display_to_dos():
    if not to_dos:
        print("No to-dos yet.")
    for index, item in enumerate(to_dos, start=1):
        print(f"{index}- {item['title']} - {item['created_at']} - {'Done' if item['is_done'] else 'Not Done'}")
        is_done_input = input("Is this done? y for yes, n for no: ").lower().strip()
        if is_done_input == "y":
            to_dos[index - 1]["is_done"] = True
    input("Press Enter to continue...")


def search_to_dos():
    search = input("Search for: ")
    found_results = list(filter(lambda item: search.lower() in item['title'].lower(), to_dos))
    print(f"Found results: {len(found_results)}")
    for item in found_results:
        print(f"- {item['title']}")
    input("Press Enter to continue...")


def save_and_exit():
    print("Goodbye mate!")
    with open("to_dos.json", "w", encoding="utf-8") as file:
        content = json.dumps(to_dos, indent=2)  
        file.write(content)
    exit()


usage = '''
1- Add to-do list.
2- Display your to-dos.
3- Search your to-dos.
4- Exit.
'''

while True:
    user_choice: str = input(usage)
    if user_choice == "1":
        add_to_do()
    elif user_choice == "2":
        display_to_dos()
    elif user_choice == "3":
        search_to_dos()
    elif user_choice == "4":
        save_and_exit()
    else:
        print("Please choose a valid choice.")
