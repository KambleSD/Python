import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return True
        elif you == 's':
            return False
    elif comp == 'g':
        if you == 's':
            return True
        elif you == 'w':
            return False

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'

while True:
    You = input("Your Turn: Snake(s) Water(w) or Gun(g)?").lower()
    if You not in ('s', 'w', 'g'):
        print("Invalid input. Please enter s, w, or g.")
    else:
        break

a = gameWin(comp, You)

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")   
else:
    print("You Lose!")
