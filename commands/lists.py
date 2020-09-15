import os.path
import json
from datetime import datetime

File_Name = 'lists.json'


def show_lists(args): 
    with open(File_Name,'r') as list_json:
        try:
            data = json.load(list_json)
            for index, todo_list in enumerate(data.keys()):
                print(index+1, data[todo_list]['title'])
        except:
            print('Some error occurred!')


def use_lists(args):
    if not args:
        #print("invalid list name")
        return -1
    list_name =args[0]
    #print("here: ",list_name)
    with open(File_Name, 'r') as lists_json:
        try:
            #print("rm")
            data = json.load(lists_json)
            #print(data, data.get(list_name))
            if(data.get(list_name)):
                return f'{list_name}.json'
            else:
                return -1
        except:
            print('Some error occurred!')

    #print("ram") 
def create_lists(args):
    list_name =args[0]
    #print(list_name)
    #print(os.path.abspath('.'))
    new_list = {}
    with open(File_Name,'r+') as lists_json:
        try:

            #check if file already exists
            data = json.load(lists_json)
            if data.get(list_name):
                print('List already exists! Try a diffrent name...')
            else:
                #update the new_list dic
                new_list ={
                    'title':list_name,
                    'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }
                data[list_name]=new_list

                #print("till correct1")
                with open(f'lists/{list_name}.json','w') as new_list:
                    #empty list
                    new_list.write('[\n]')
                    print('Successfully created the new list!')
                #add to the lists.json
                lists_json.seek(0)
                json.dump(data, lists_json, sort_keys=True, indent=True)

        except:
            print('Some error occurred!')



    #print("ram2")