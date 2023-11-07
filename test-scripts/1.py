def greet(name):    
    return print('Fuck you and the horse you rode in on, ' + name + '!')

def promptForName():
    name = input('What\'s your name? ')
    return name

def main():
    repeat = True
    while repeat:
        yourName = promptForName()
        greet(yourName)
        if input('Enter y to play again or any key to exit ').lower() != 'y':
            repeat = False 

if __name__ == '__main__':
    main()
