# Todo CLI application

## Use cases, running our application => commands
- structuring our code
- implemation along with testing
- run and use it :)


## use cases
- create a todo list
- show all the todo lists
- Add , edit, delete, mark as complete, incomplete etc
the todo items presents in thoses lists\
-show all the todo items in a perticular list


## commnds to use the CLI app

=> prefixes for the commands : list, todo
example:
lists = ['course', 'course2', 'course3]
'course1' => todo['read a', 'read b'  ]
- list show all the todo lists we have
- list create list_name => create a list with list_mame
- list use list_name => select perticular todo list

- todo add todo_item
- todo all => show all todos in slected list item_id
- todo edit item_id  new_title
- todo remove item_id
- todo complete item_id
- todo incoplete item_id => mark the task with item id as incomplete

- help => print all the commmands we can use for cli commands
- quit command

## Data

### Lists.json
- stores a list of todo lists
[
    'list1',
    'list2'
]

check whether a given list exits
=> using the above appraoch , need to iterate over all list elements

- a seperate json file for each list
data = {
    'title':{
        'file_name': 'name'
        'create_at': time
    }
}

data['list1']['created_at']

=> checking if list exits title key exits or not

### list1.joson 

- list of todo items
[
    {
        'title': 'name',
        'crate_at': 'time,
        'completed': false
    }
]

-  serialize and deserialize the data og json file







