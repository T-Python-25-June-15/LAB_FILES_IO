from datetime import datetime
import json
class RangeError(Exception):
    'raise error if user enter number not in range of to do list'

to_dos:list = []
try:
    with open('to_dos.json', 'r', encoding="UTF-8") as file:
        content = file.read()
        to_dos = json.loads(content) #Decode
except Exception as e:
    pass

def add_todo():
    title = input('name a title of todo: ')
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_do_item = {
        'title': title,
        'created_at': created_at,
        'is_done': False,
    }
    to_dos.append(to_do_item)
    print("added!")


def display_todo_list(to_dos: list):
    for i, item in enumerate(to_dos, start=1):
        print(f"{i}.{item['title']} {item['created_at']} {'Done' if item['is_done'] else 'Not Done'}")


def mark_done():
    display_todo_list(to_dos)
    try:
        is_done = int(input('enter number of todo to change it Done or Not Done: '))
        if is_done <= len(to_dos):
            state = to_dos[is_done - 1]['is_done']
            to_dos[is_done - 1]['is_done'] = False if state else True
        else:
            raise RangeError('please enter number in the range')
    except RangeError as e:
        print(e)
    else:
        print('you compleat your task nice!!')


def searching(title: str):
    result = []
    for item in to_dos:
        if title in item['title']:
            result.append(item)
        
    if len(result) == 0:
        print(f'Sorry we not found {title} in your to do list')
    else:
        print(f'---we find the title: {title} in this list---')
        display_todo_list(result)

usage = '''
1- add to do list.
2- display your to dos.
3. mark as done or not
4- search your to dos.
5- exit
'''

def main():
    while True:
        user_choise = input(usage)
        if user_choise == '1':
            add_todo()

        elif user_choise == '2':
            display_todo_list(to_dos)
        
        elif user_choise == '3':
            mark_done()

        elif user_choise == '4':
            searching(input('searching for title :'))

        elif user_choise == '5':
            with open('to_dos.json', 'w', encoding='UTF-8') as file:
                json.dump(to_dos, file, indent=2)
                break

main()

    
