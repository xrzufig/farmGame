import random

class Farm(object):

    global size
    size = 100
    global lvl
    lvl = 1

    def __init__(self, countChicken, food, countCow, cowFood, size):
        self.countChicken = countChicken
        self.food = food
        self.countCow = countCow
        self.cowFood = cowFood
        self.size = size


    def feedAnimals(self, countChicken, countCow ,food, cowFood):
        print('food: ', food, ', cow food: ', cowFood)
        print('animals: ', countChicken, ' ', countCow)
        feeded = food - countChicken - countCow - cowFood
        print('food after feeding: ', feeded)

class Randomize(object):

    def __init__(self, countCow, cowFood):
        self.countChicken = countChicken
        self.food = food
        self.countCow = countCow
        self.cowFood = cowFood

    def weather(self):
        pass

    def field(self):
        pass

    def harvest(self):
        pass

    def animalRandomFood(self, countCow, cowFood):
        pass

    def gamerLevel(self):
        pass
    
    
    def animalRandomSelection(self, countChicken, food, countCow, cowFood):
        r = random.randint(1, 100)
        print(r)
        if r >= 1 and r <= 15:
            rDelete = random.randint(1, 2)
            if rDelete == 1:       
                if self.countChicken == 0:
                    self.countChicken -= 0
                else:
                    self.countChicken -= 1
            elif rDelete == 2:
                if self.countCow == 0:
                    self.countCow -= 0
                else:
                    self.countCow -= 1
            self.food += 9
            print('* u lost animals: ', self.countChicken, 'gain food: ', self.food, '*')
        elif r >= 16 and r <= 41:
            self.countChicken += 1
            print('* u gain animals: ', self.countChicken, 'gain food: ', self.food, '*')
        elif r >= 42 and r <= 67:
            self.countCow += 1
            print('* u lost animals: ', self.countCow)
        else:
            print('nothing happend')