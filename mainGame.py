from functions import Farm, Randomize
import time

def nameInput():
    print('Hello to ur new farm!')
    name = input('Enter ur farmer name below!\n> ')
    print('hello ', name)

nameInput()

chicken = 50
chickenFood = 250
cow = 50
cowFood = 250


for i in range(5):
    print("## ", i+1, " ##")
    Randomize.animalRandomSelection(0, chicken, chickenFood, cow, cowFood)
    Farm.feedAnimals(0, chicken, cow, chickenFood, cowFood)
    Randomize.harvest(100, 100)