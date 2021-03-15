import sys
import time
import os

def preLoader():
    while True:
        try:
            print('\nPre-Loader')
            print('1:main')
            print('2:save test')
            print("")
            varpre = int(input(""))
            if varpre == 1:
                restOf()
            if varpre == 2:
                cb = open('playerdat.txt', 'r')
                lines = cb.readlines()
                name = lines[0] #note that lines start at 0, e.g. line number 4 is 'lines[3]'
                strength = lines[1]
                mag = lines[2]
                char = lines[3]
                agi = lines[4]
                race = lines[5]
                cb.close()
                print("Name is set to ", name)
                print("Strength value = ", strength)
                print("Magick value = ", mag)
                print("Charisma value = ", char)
                print("Agility value = ", agi)
                print("Race value = ", race)
                print('')
                time.sleep(5)
                preLoader()
        except ValueError:
            print('\nHey dumbass, try not to hit other buttons, alright?')
            time.sleep(0.5)
            preLoader()

def restOf():
    strength = 0
    mag = 0
    char = 0
    agi = 0
    name = 0
    race = 0
    print("\nThe Ragnarok TBB Character Creator")
    print("Enter The Ragnarok?")
    print("N/Y")
    var0 = input("")
    if var0 == "N":
        sys.exit()
    if var0 == "Y" or "y":
        print("Welcome to the Ragnarok")
        time.sleep(0.05)
        print("Pick your worthless class")
        print("5:Fighter")
        print("4:Boxer")
        print("1:Catgirl")
        print("2:Mage (if you choose this, you suck)")
        print("3:Ranger")
        print("6:Catgirl (autistic)")
        print("7:Catboy")
        print("8:Catboy (autistic)")
        print("")
        varclass = int(input(""))
        if varclass == 5:
            strength = 10
            mag = 3
            char = 3
            agi = 1
            race = 'fighter'
            print("You are a Fighter")
        if varclass == 4:
            strength = 13
            mag = 0
            char = 2
            agi = 5
            race = 'boxer'
            print("You are a Boxer")
        if varclass == 1:
            strength = 3
            mag = 3
            char = 10
            agi = 14
            race = 'catgirl'
            print("You are a Catgirl")
        if varclass == 2:
            strength = 0
            mag = 15
            char = 0
            agi = 0
            race = 'mage'
            print("You have chosen a very stupid class. Shame on you.")
        if varclass == 3:
            strength = 4
            mag = 6
            char = 5
            agi = 12
            race = 'ranger'
            print("You are a Ranger! I love you.")
            time.sleep(1)
            print("Sowwy UwU")
        if varclass == 6:
            strength = 7
            mag = 14
            char = 0
            agi = 14
            race = 'autisticcatgirl'
            print("You are, indeed, an autistic Catgirl.")
        if varclass == 8:
            strength = 9
            mag = 14
            char = 0
            agi = 12
            race = 'autisticcatboy'
            print("You are, indeed, an autistic Catboy.")
        if varclass == 7:
            strength = 5
            mag = 3
            char = 10
            agi = 12
            race = 'catboy'
            print("You are a Catboy")
        print("Your Strength is", strength)
        print("Your Magical ability is", mag)
        print("Your Charisma is", char)
        print ("your agility is ", agi)
        if varclass == 2:
            print("What is your name")
            name = input()
        if varclass != 2:
            print("what is your name hero?")
            name = input()
        print("Hello, ", name)
        print("Saving...")
        cb = open("playerdat.txt","w+")
        cb.write(name)
        cb.write("\n")
        cb.write(str(strength))
        cb.write("\n")
        cb.write(str(mag))
        cb.write("\n")
        cb.write(str(char))
        cb.write("\n")
        cb.write(str(agi))
        cb.write("\n")
        cb.write(str(race))
        cb.close()
        sys.exit()

preLoader() #exec
