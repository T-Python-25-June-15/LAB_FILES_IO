import json
from datetime import datetime

CYAN = "\033[36m"
RESET = "\033[0m"

notes_list = []

def readJSONFile():
    try:
        with open('to_do.json', 'r', encoding="utf-8") as reader:
            global notes_list
            notes_list = json.loads(reader.read())
    except:
        pass

def writeJSONFile():
    try:
        with open('to_do.json', 'w', encoding="utf-8") as writer:
            writer.write(json.dumps(notes_list, indent=2))
    except:
        pass
    
def printHomePage():
    print(CYAN + "\n" + "-"*100 + "\n")
    print("1. Add a note\n2. View notes\n3. Delete a note\n4. Mark notes\n5. Exit")
    print("\n" + "-"*100 + "\n" + RESET)

def addNote():
    title = input("Title: ")
    date_time = datetime.now().strftime("Date: %d/ %m/ %Y - Time: %H:%M")
    notes_list.append({
        "title": title,
        "date": date_time,
        "done": False
    })

def viewNotes():
    for index, item in enumerate(notes_list, start=1):
        print(f"{index}. {item["title"]} - {item["date"]} - {" ✓".rjust(50 - len(item["title"]), ".") if item["done"] else " ✕".rjust(50 - len(item["title"]), ".")}")


def deleteNote():
    print()
    viewNotes()
    _input = int(input("Enter the number of the note you want to delete.\n>>> "))
    for i, item in enumerate(notes_list, start=1):
        if i == _input:
            notes_list.remove(item)
            break

def markNotes():
    for i, item in enumerate(notes_list, start=1):
        print(f"{i}. {item["title"]}{" ✓".rjust(20 - len(item["title"]), ".") if item["done"] else " ✕".rjust(20 - len(item["title"]), ".")}")
        user_in = input("Are you done? y for yes and n for no: ").lower()
        if user_in  == 'y':
            item["done"] = True
        elif user_in  == 'n':
            item["done"] = False
            
    input("\n...Press anything to continue")

def main():
    readJSONFile()
    
    while True:
        printHomePage()
        try:
            user_input = int(input("Enter your choice: "))
            match user_input:
                case 1: addNote()
                case 2: 
                    viewNotes() 
                    input("\n...Press anything to continue")
                    
                case 3: deleteNote()
                case 4: markNotes()
                case 5: break
                case _: print("Invalid number, please try again.")
            
        except:
            print("Invalied input, please try again.")
    
    writeJSONFile()
        

main()
        # list comperhentio 
        # new_list = [f for f in list() if f > 5]