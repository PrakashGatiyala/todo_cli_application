import json
from datetime import datetime

def set_list(list_name):
    if list_name=='':
        print('Please select a given list before this action')
    return list_name


def get_data(list_name):
    
    with open(f'lists/{list_name}','r') as todo_list:
        data = json.load(todo_list)
    return data

def update_data(list_file_name, data):
    with open(f'lists/{list_file_name}','w') as json_file:
        json.dump(data, json_file, sort_keys=True, indent=True)


def add_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    
    data = get_data(list_name)
    title = args[1]
    data.append({
        'title':title,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'completed': False
    })
    #add this todo item
    with open(f'lists/{list_name}','w') as todo_list:
        json.dump(data,todo_list, sort_keys=True, indent=True)
        

def show_items(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    
    data = get_data(list_name)
    complete=0
    if(len(data)==0):
        print('No todo item in this list')
        return 

    for index, todo_item in enumerate(data):
        print(index+1, todo_item['title'])
        if todo_item['completed']:
            complete+=1
    print(f'{complete}/{len(data)} completed!')
    
    
def edit_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    new_title = args[2]
    data = get_data(list_name)

    updated_todo= {
        'title': new_title,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'completed': False

    }

    data[item_id-1]=updated_todo
    update_data(list_name,data)

    #print("No")

def remove_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data.pop(item_id-1)
    update_data(list_name,data)
    #print("No")

def complete_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data[item_id-1]['completed']=True
    update_data(list_name,data)
    #print("No")

def incomplete_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data[item_id-1]['completed']=False
    update_data(list_name,data)

    #print("No")