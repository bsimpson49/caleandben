# Hello, world! test file

def greet(name: str) -> str:
    return print('Fuck you and the horse you rode in on, ' + name + '!')

def promptForName() -> str:
    name = input('What\'s your name? ')
    return name

if __name__ == '__main__':
    repeat = True
    while repeat:
        yourName = promptForName()
        greet(yourName)
        if input('Enter y to play again or any key to exit ').lower() != 'y':
            repeat = False 

