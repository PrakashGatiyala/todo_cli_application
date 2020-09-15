#Todo CLI application

-Use cases, running our application => commnds
- structuring our code
- implemation alogn with testing
- run and use it :)


#use cases
- create a todo list
- show all the todo lsits
- Add , edit, delte, amrks a complte, incomple tcs
the tood itesm presents in thoses lists\
-shoe all the tod items in a articular items


# commnds to use the CLI app

=> prefices for tje commnds : list, todo

lists = ['course', 'course2', 'course3]
'course1' => todo['read a'1  ]
- list show all the todo lists we have
- list create list_ma,e => create a list wiht list_mame
- list use list_name => select apartuclt todo list

-  todo add todo_tiple
- todo all => show all toods in slected list item_id
- todo edit item_id  new_title
- todo remove item_id
- todo compete item_id
- todo incoplte item_id => makrs the utesm wihr item id as incomplte

- help => print all the commmnds we cn use out app
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

- a seperate josn file for each list
data = {
    'title':{
        'file_name': 'name'
        'create_at': time
    }
}

data['list1']['created_at']

=> checking if alist exits title key exits or not

### list1.joson 

- list of todo ites
[
    {
        'title': 'name',
        'crate_at': 'time,
        'completed': false
    }
]

-  seralize and deseriliaze te data








