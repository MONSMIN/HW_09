
contacts = {'Dima': [+30000001],'Patron': [+38888888888]}

def input_error(func):
    
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Print help"
    return inner




@input_error
def add(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_number = list_of_param[1:]
    contacts.update({name:phone_number})
    if not phone_number:
        raise IndexError()
    
    return f'{name}, phone number {phone_number}'

def show_all(*args):
    return '\n'.join(f'{k}: {str(v[0])}' for k, v in contacts.items())


@input_error
def phone(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    for k, v in contacts.items():
        if k == name:
            return f'phone number: {str(v[0])}'

@input_error
def change(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_number = list_of_param[1:]
    for k , v in contacts.items():
        if name == k:
            contacts[k] = phone_number

            return f'Contact {k} update {str(phone_number[0])}'

def exit(*args):
    return "Good bye!"

def no_command(*args):
    return 'Unknown command, try again or help'

def help(*args):
    return "If there are problems, read the file, readme!"

def hello(*args):
    return "How can I help you?"

COMMANDS = {help: 'help',
            hello: 'hello',
            add: 'add',
            show_all: 'show all',
            phone: 'phone',
            change: 'change',
            exit: 'exit'}


def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None


def main():
    print('Hello user!')
    while True:
        
        user_input = input('>>>')
        command, data = command_handler(user_input)

        print(command(data))
        
        if user_input == 'exit':
            break 
            



if __name__ == '__main__':
    main()