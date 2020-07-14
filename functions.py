import random

class Farm(object):

    def __init__(self, countChicken, food, countCow, cowFood, size):
        self.countChicken = countChicken
        self.food = food
        self.countCow = countCow
        self.cowFood = cowFood
        self.size = size


    def feedAnimals(self, countChicken, countCow ,food, cowFood):
        rToFeed = random.randint(1, 100)
        print('ur food: ', food)
        toFeed = input('do you want to feed chickens, [y/n]:  ')

        if toFeed == 'n':
            if rToFeed == 77:
                countCow -= 15
            else:
                print('ok')
        else:
            feeded = food - countChicken
            print(feeded)

    def gamerLevel(self, countCow, countChicken):
        lvl = 1
        fieldSize = 100
        if countCow >= 25 and countCow >= 25:
            lvl = 2
            fieldSize += 100 
            print('u hit lvl 2')
        elif countCow >= 50 and countCow >= 50:
            fieldSize += 100 
            lvl = 3
            print('u hit lvl 3')
        elif countCow >= 75 and countCow >= 75:
            fieldSize += 100 
            lvl = 4
            print('u hit lvl 4')
        elif countCow >= 100 and countCow >= 100:
            fieldSize += 100 
            lvl = 5
            print('u hit lvl 5')

        
    def weekTime(self):
        pass

class Randomize(object):

    def __init__(self, countCow, countChicken, cowFood, chickenFood):
        self.countChicken = countChicken
        self.chickenFood = chickenFood
        self.countCow = countCow
        self.cowFood = cowFood

    def field(self):
        pass

    def harvest(self, fieldSize):
        rWeather  = random.randint(1, 4)
        if rWeather == 1:
            raining = True
            print('Its raining')
        else:
            raining = False
        if rWeather == 2:
            sunny = True
        else:
            sunny = False
        if rWeather == 3:
            cloudy = True
        else:
            cloudy = False
        if rWeather == 4:
            storm = True
        else:
            storm = False

        money = 0
        if fieldSize == 100:
            print('field size: ', fieldSize)
            if raining:
                money += 15
                print('Its raining')
            else:
                pass
            if sunny:
                money += 50
                print('Its sunny')
            if cloudy:
                money += 30
                print('Its cloudy')
            if storm:
                money += 5
                print('Its storm')
        if fieldSize == 200:
            print('field size: ', fieldSize)
            if raining:
                money += 20
                print('Its raining')
            if sunny:
                money += 60
                print('Its sunny')
            if cloudy:
                money += 40
                print('Its cloudy')
            if storm:
                money += 10
                print('Its storm')
        if fieldSize == 300:
            print('field size: ', fieldSize)
            if raining:
                money += 25
                print('Its raining')
            if sunny:
                print('Its sunny')
                money += 70
            if cloudy:
                money += 50
                print('Its cloudy')
            if storm:
                money += 15
                print('Its storm')
        if fieldSize == 400:
            print('field size: ', fieldSize)
            if raining:
                money += 30
                print('Its raining')
            if sunny:
                print('Its sunny')
                money += 80
            if cloudy:
                money += 60
                print('Its cloudy')
            if storm:
                money += 20
                print('Its storm')
        if fieldSize == 500:
            print('field size: ', fieldSize)
            if raining:
                money += 35
                print('Its raining')
            if sunny:
                print('Its sunny')
                money += 90
            if cloudy:
                money += 70
                print('Its cloudy')
            if storm:
                money += 40
                print('Its storm')
        print('gained money: ', money)

    def animalRandomFood(self, cowFood, chickenFood):
        rFood = random.randint(1, 100)
        print(rFood)
        if rFood >= 1 and rFood <= 25:
            cowFood += 15
            chickenFood += 15
        if rFood >= 16 and rFood <= 75:
            cowFood += 10
            chickenFood += 10
        if rFood >= 76 and rFood <= 100:
            cowFood += 25
            chickenFood += 25

    def animalRandomSelection(self, countChicken, chickenFood, countCow, cowFood):
        r = random.randint(1, 100)
        print('ur chickens: ', countChicken)
        print('ur chicken food: ', chickenFood)
        print('ur cows: ', countCow)
        print('ur cow food: ', cowFood)
        if r >= 1 and r <= 15:
            rDelete = random.randint(1, 2)
            if rDelete == 1:       
                if countChicken == 0:
                    countChicken -= 0
                else:
                    countChicken -= 1
            elif rDelete == 2:
                if countCow == 0:
                    countCow -= 0
                else:
                    countCow -= 1
        elif r >= 16 and r <= 41:
            countChicken += 1
            print('* u gain animals: ', countChicken, '*')
        elif r >= 42 and r <= 67:
            countCow += 1
            print('* u lost animals: ', countCow)
        else:
            print('nothing happend')