import          json
from            datetime        import      datetime


datetimevalue = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


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
        try:

            print("""
                    1- Add To-Do Task
                    2- Show To-Do Tasks
                    3- Edit To-Do Task
                    4- Exit
                """)

            question = int(input("\nSelect your to-do option: "))

            match question:
                case 1:
                    title = input("To-Do Title: ")
                    dataToSave = {title: {'date': datetimevalue,'done':False}}
                    writejson(filepath,dataToSave)

                case 2:
                    data = readjson(filepath)
                    for todoIndex,todo in enumerate(data):

                        if data[todo]['done'] == True:
                            status = "Done"
                        else:
                            status = "Not Done"

                        print(f"{todoIndex+1}- {todo} - {data[todo]['date']} - {status}")

                case 3:
                    markItDone = int(input("Select your to-do task to mark it done: "))
                    data = readjson(filepath)

                    for todoIndex,todo in enumerate(data):

                        if (todoIndex +1) == markItDone:           
                            if data[todo]['done'] == True:
                                print("This task already done! ")
                            elif data[todo]['done'] == False:
                                data[todo]['done'] = True  
                                writejson(filepath, data)
                                print(f"Marked to-do Number {markItDone} as done.")
                            else:
                                print("Something went wrong!")

                case 4:
                    print("\nthank you for using the To-Do program, come back again soon\n")
                    break

            # if question == 'exit':
            #     print("\nthank you for using the To-Do program, come back again soon\n")
            #     break

            # if question == 'y' or question == 'yes':
            #     title = input("To-Do Title: ")
            #     dateInput = date
            #     dataToSave = {title: {'date': dateInput,'done':False}}
            #     writejson(filepath,dataToSave)

            # elif question == 'n' or question == 'no':
            #     question2 = input("\ndo you want to list your To-Do items (y:yes and n:no) ? ")
            #     if question2 == 'exit':
            #         print("\nthank you for using the To-Do program, come back again soon\n")
            #         break

            #     if question2 == 'y' or question2 == 'yes':
            #         data = readjson(filepath)
            #         for todoIndex,todo in enumerate(data):

            #             if data[todo]['done'] == True:
            #                 status = "Done"
            #             else:
            #                 status = "Not Done"
            #             print(f"{todoIndex+1}- {todo} - {data[todo]['date']} - {status}")
            # else:
            #     print("wrong option")
        except Exception as ex:
            print(ex)
main()