import json
from datetime import datetime

to_dos:list= []

try:
    with open('LAB_FILES_IO/to_do.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        to_dos= json.loads(content)
except Exception as e:
    print("file not found")




msg = input('''Welcome !
1-Add new task
2-List tasks
3-mark task as done
4-search for task 
5-Exit \n''')

while msg != 'exit':
    if msg == '1':
    
       todo_title = input("enter you To-do title:")
       to_dos.append({
           'title':todo_title,
           "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": False
       })
       print("To-Do item added successfully!")
        

    elif msg == '2':
        print('-------------------')
        for i,task in enumerate(to_dos):
            print(f"{i}- {task['title']} - {task['date']} - {'Done' if task['status']  else 'Not Done'}")
        print('-------------------')

        

    elif msg == '3':
        taskTitle= input('enter task title:')
        found = False
        for task in to_dos:
            if task['title'] == taskTitle:
                task['status']= True
                found = True
                break

        if found == False:
            print("not found!")

        
   

    elif msg == '4':
        search= input("enter task title:")
        found_results = [task for task in to_dos if search.lower() in task['title'].lower()]
        print(f"{len(found_results)} results found! \n")
        for i,item in enumerate(found_results):
            i+=1
            print(f"{i}- {item['title']} - {item['date']} - {'Done' if item['status']  else 'Not Done'}")
        
        
    


    elif msg == '5':
        with open('LAB_FILES_IO/to_do.json','w', encoding='UTF-8') as File:
            content = json.dumps(to_dos, indent=2)
            File.write(content)
            File.close()
            break
            

    msg = input('''Welcome !
1-Add new task
2-List tasks
3-mark task as done
4-search for task 
5-Exit \n''')


