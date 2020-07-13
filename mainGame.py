from functions import Farm, Randomize

def nameInput():
    print('Hello to ur new farm!')
    name = input('Enter ur farmer name below!\n> ')
    print('hello ', name)

nameInput()

Randomize.animalRandomSelection(0, 50, 5, 50, 50)
Randomize.harvest(100, 100)