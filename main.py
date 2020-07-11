import random

class Farm(object):

    def __init__(self, countChicken, food, countCow, cowFood):
        self.countChicken = countChicken
        self.food = food
        self.countCow = countCow
        self.cowFood = cowFood

    def feedAnimals(self, countChicken, countCow ,food, cowFood):
        countOfAnimals = self.countChicken + self.countCow
        haveFood = self.food
        haveCowFood = self.cowFood
        """
        if countOfAnimals > 100:
            print('u cant have more than 100 animals')
            countChicken = 100
        else:
            countChicken = countOfAnimals
        if haveFood > 500:
            print('u cant have more than 500 kg of food')
            food = 500
        else:
            food = haveFood
        """

        print('food: ', food, ', cow food: ', cowFood)
        print('animals: ', countChicken, ' ', countCow)
        feeded = food - countChicken - countCow - cowFood
        print('food after feeding: ', feeded)

    def animalLifesChicken(self, countChicken, food):
        r = random.randint(1, 50)
        print(r)
        if r >= 1 and r <= 10:
            if self.countChicken == 0:
                self.countChicken -= 0
            else:
                self.countChicken -= 1
            self.food += 9
            print('* u lost animals: ', self.countChicken, 'gain food: ', self.food, '*')
        elif r >= 11 and r <= 20:
            self.countChicken += 1
            self.food += 11
            print('* u gain animals: ', self.countChicken, 'gain food: ', self.food, '*')
        elif r >= 21 and r <= 30:
            if self.countChicken == 0:
                self.countChicken -= 0
            self.food += 3
            print('* u lost animals: ', self.countChicken, 'gain food: ', self.food, '*')
        elif r >= 31 and r <= 40:
            self.countChicken += 2
            self.food += 18
            print('* u gain animals: ', self.countChicken, 'gain food: ', self.food, '*')
        else:
            self.countChicken += 5
            self.food += 15
            print('* u gain animals: ', self.countChicken, 'gain food: ', self.food, '*')

    def animalLifesCow(self, countCow, cowFood):
        r = random.randint(1, 100)
        if r >= 1 and r <= 7:
            self.countCow += 3
            self.cowFood += 15
            print('cows: ', self.countCow)
            print('food: ', self.cowFood)
        elif r >= 8 and r <= 13:
            self.countCow -= 2
            self.cowFood += 15
            print('food: ', self.cowFood)
            print('cows: ', self.countCow)
        elif r >= 14 and r <= 17:
            self.countCow += 4
            self.cowFood += 15
            print('food: ', self.cowFood)
            print('cows: ', self.countCow)
        elif r >= 18 and r <= 25:
            self.countCow -= 1
            self.cowFood += 15
            print('food: ', self.cowFood)
            print('cows: ', self.countCow)
        elif r == 77:
            self.cowFood += 15
            self.countCow += 15
            print('food: ', self.cowFood)
            print('cows: ', self.countCow)
        else:
            self.cowFood += 15
            self.countCow += 1
            print('food: ', self.cowFood)
            print('cows: ', self.countCow)

"""       
count = 20
countcows = 20
food = 200
cowFood = 200
f = Farm(0, 0, 0, 0)
for i in range(4):
    print('### ', i+1, ' ###')
    f.feedAnimals(count, countcows, food, cowFood)
    f.animalLifesChicken(count, food)
    f.animalLifesCow(countcows, cowFood)
"""

f = Farm(0,0,0,0)
print(f.animalLifesCow(20, 100))