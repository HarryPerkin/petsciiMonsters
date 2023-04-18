# A cute little game about levelling up an ASCII pet.

# First import 'keyboard', which will allow the registering of keystrokes.
import keyboard, time, os, sys, random
import asciiGameData as r

# Utility Variables
width = os.get_terminal_size().columns # Get terminal width.

gameProgress = [] # Initialised. Contents generated below.
prestigeCount = 0

# Main Game Loop.
def main():

    # Game Variables
    power = {'a': 0, 'd': 0, 'z': 0}
    petID = 0


    while True:
        clearScreen()
        print(f" Your current monster is No.{petID}: {r.idList[petID]}\n")
        print(" A POWER: " + str(power['a']) + "\tD POWER:" + str(power['d']) + "\tZ POWER:" + str(power['z']))
        printPet(petID, 0, False)
        
        
        # Listens for the correct keystrokes.
        if keyboard.read_key() == "p": # Reports the player's progress.
            printProgress()
            
        elif keyboard.read_key() == "a":
            power['a'] += 1
            
        elif keyboard.read_key() == "d":
            power['d'] += 1
           
        elif keyboard.read_key() == "z":
            power['z'] += 1
            
        elif keyboard.read_key() == "r":
            if prestige() == True:
                prestigeCount += 1
                power = {'a': 0, 'd': 0, 'z': 0}
                petID = 0
        elif keyboard.read_key() == "q":
            print("Exiting. Thank you for playing!")
            quit()
        elif keyboard.read_key() == "c":
            coinFlip()
            
            
            
        # Next are the score thresholds for the monsters.
        if petID == 0 and power == {'a': 0, 'd': 0, 'z': 5}: # no2. Plumpkin
            if (printPet(1, 0.2, True)) == True:
                petID = 1
                print(f"Your {r.idList[0]} evolved into a {r.idList[1]}!\n".center(width))
                pressSpace()
            continue
        elif petID == 0 and power == {'a': 5, 'd': 0, 'z': 0}: # no3. Buckip
            if (printPet(2, 0.2, True)) == True:
                petID = 2
                print(f"Your {r.idList[0]} evolved into a {r.idList[2]}!\n".center(width))
                pressSpace()
            continue
        elif petID == 1 and power == {'a': 0, 'd': 0, 'z': 15}: # no5. Jackpatch
            if (printPet(4, 0.2, True)) == True:
                petID = 4
                print(f"Your {r.idList[1]} evolved into a {r.idList[4]}!\n".center(width))
                pressSpace()
            continue
        


# Generate size of progress list from size of r.roster.
for i in range(len(r.roster)):
    gameProgress.append(False)

# Functions #

def printEgg(): # Prints only when the game begins or the player prestiges.
    for i in r.roster[0]:
        print(i.center(width))
        time.sleep(0)
    time.sleep(1)

def printPet(n, t, e): # This function prints ASCII art that is stored in a 2D array. n = petID, t = print time, e = evolve bool.    
    if e == True: #  Re-added conditional block in v10. e, for evolution, passed into function.
        for c in r.evoMessage: 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
            
        print("\nWould you like to evolve your pet? Select 'N' to continue to power it up. Y/N")
        while True: # Checks before it evolves.
            answer = input().upper()
            if answer == "Y":
                break
            elif answer == "N":
                return False
    
    for i in r.roster[n]: # The actual printing.
        print(i.center(width))
        time.sleep(t)
    time.sleep(0.5)
    gameProgress[n] = True # Suitable here because game only prints when progress is made.
    return True
 
def printProgress():
    p = gameProgress.count(1)
    print(f"You have collected {p} monster(s) out of a total {len(gameProgress)}!".center(width))
    print(f"You have prestiged {prestigeCount} time(s) so far.\n".center(width))
    pressSpace()

def clearScreen(): # Clears the console. Useful for making a blank canvas!
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pressSpace(): # Prompts and waits for the user to press space. Generic Message.
    print("Press the spacebar to continue.".center(width))
    keyboard.wait("spacebar")
    
def coinFlip():
    for x in range(3):
        for i in r.coin:
            time.sleep(0.3)
            clearScreen()
            for j in i:
                print(j.center(width))
    result = random.randint(0, 1)
    clearScreen()
    time.sleep(0.3)
    if result == 0: # REDUCE REDUNDANCY HERE
        for i in r.coin[2]:
            print(i.center(width))
        print("Heads!".center(width))
    else:
        for i in r.coin[2]:
            print(i.center(width))
        print("Tails!".center(width))
    time.sleep(0.3)
    pressSpace()
    
def prestige(): # Resets the monster to an egg, but keeps progress.
    print("Are you sure you want to prestige? Progress will be kept but you will begin again from an egg. Y/N")
    while True:
        answer = input().upper()
        if answer == "Y":
            break
        elif answer == "N":
            return False
    
    clearScreen()
    printEgg()
    
    print("Press the spacebar to begin again. This time try different combinations of power!".center(width))
    keyboard.wait("spacebar")
    return True

# Instructions.
clearScreen()
print("Press P to view your progress, R to prestige, C to flip a coin, and Q to quit!".center(width))
print("INSTRUCTIONS: Repeatedly tap A, D, or Z to encourage your pet to grow!\n".center(width))
printEgg() # Begins the game by printing a picture of your egg.
print("Press the spacebar to begin.".center(width))
keyboard.wait("spacebar")



main()

print(f"Congratulations on collecting every monster! You managed it by prestiging {prestigeCount} times!".center(width))
