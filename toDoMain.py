import json

filepath = 'data.json'

def readjson(path):
    with open(path,'r') as file:
        return json.load(file)

def writejson(path,data):
    try:
        with open(path,'r') as file:
            olddata = json.load(file)

            olddata.update(data)
        
        with open(path,'w') as f:
            json.dump(olddata, f, indent=2)
    except:
        olddata = {}

def main():
    while True:
        question = input("\ndo you want to add a new To-Do item (y:yes and n:no) ?: ")
        if question == 'exit':
            print("\nthank you for using the To-Do program, come back again soon\n")
            break

        if question == 'y' or question == 'yes':
            title = input("To-Do Title: ")
            date = input("To-Do Date example(mm/dd/yy): ")
            time = input("To-Do Time example(00:00 AM): ")
            data = {title: {'date': date,'time':time,'done':False}}
            writejson(filepath,data)

        elif question == 'n' or question == 'no':
            question2 = input("\ndo you want to list your To-Do items (y:yes and n:no) ? ")
            if question2 == 'exit':
                print("\nthank you for using the To-Do program, come back again soon\n")
                break

            if question2 == 'y' or question2 == 'yes':
                data = readjson(filepath)
                for todo in data:

                    if data[todo]['done'] == True:
                        status = "You did it"
                    else:
                        status = "Not yet"
                    print(f"\n{todo} - {data[todo]['date']} {data[todo]['time']} - {status}\n")
        else:
            print("wrong option")

main()