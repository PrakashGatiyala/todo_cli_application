from commands import commands_dict


def parse(command):
  command_list = command.split()
  command_type = command_list[0]

  if command_type=='quit' or command_type=='help':
    return command_type, []
  elif command_type=='todo':
    command_name = command_list[1]
    if command_name in ['all', 'complete', 'incomplete', 'remove','add','edit']:
      return command_name, command_list[2:]
    else :
      return 'invalid',[]
  elif command_type=='list':
    command_name=command_list[1]
    if command_name in ['show', 'create', 'use']:
      return command_name , command_list[2:]
    else:
      return 'invalid',[]
  else :
    return 'invalid',[] 

def main():
    print("Started the todo application...'")
    current_list=''
    while(1):
        command= input('$ ')
        #commnds_type, commnds_name,  commnd_args
        #split the string sepeated by space
        command_name, command_args = parse(command)
        if command_name=='quit':
            break
        elif command_name=='help':
          with open('help.txt','r') as f:
            print(f.read())
          #
        elif command_name =='invalid':
            print('plase enter a valid command')
            print("Use 'help' for list of valid command")
        elif command_name=='use':
          #print("wrong")
          file_name = commands_dict[command_name](command_args)
          #print("file name is: ",file_name)
          if file_name==-1:
            print('This is not a valid list name! or this list does not exists ')
            current_list=''
          else:
            print('Successfuly chosen this list....')
            current_list=file_name

            #
        elif command.split()[0]=='todo':
            #print("todo commnd")
            command_args.insert(0, current_list)
            commands_dict[command_name](command_args)
            #
        else:
            commands_dict[command_name](command_args)
if __name__ == '__main__':
    main()