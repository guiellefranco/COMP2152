# Coding Questions 02 Week 02
# First Name: Khaila, Last Name: Franco
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]

# Error handling for valid combat strength inputs
try:
    combatStrength = int(input("Enter your combat Strength: "))
    mCombatStrength = int(input("Enter the monster's combat Strength: "))
except ValueError:
    print("Error: Please enter a valid integer for combat strength.")
    exit()

input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print(f"You rolled {healthPoints} health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print(f"You rolled {mHealthPoints} health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print(f"Have you found a healing potion?: {bool(healingPotion)}")

input("Analyze the roll (Press enter)")
# Equality operators
print(f"--- You are matched in strength: {str(combatStrength == mCombatStrength)}")

# Relational operators
print(f"--- You have a strong player: {str((combatStrength + healthPoints) >= 15)}")

# and keyword
print(f"--- Remember to take a healing potion!: {str(healingPotion == 1 and healthPoints <= 6)}")

# not keyword
print(f"--- Phew, you have a healing potion: {str(not (healthPoints < mCombatStrength) and healingPotion == 1)}")

# or keyword
print(f"--- Things are getting dangerous: {str(healingPotion == 0 or healthPoints == 1)}")

# in keyword
print(f"--- Is it possible to roll 0 in the dice?: {str(0 in diceOptions)}")

# --- Expanded if statement
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print(f"--- Using your healing potion... Your Health Points is now full at {healthPoints}")
else:
    print(f"--- Your health is low at {healthPoints} and you have no healing potions available!")

# --- Nested if statement
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print(f"Your sword ({combatStrength}) ---> Monster ({mHealthPoints})")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength
    print(f"You've reduced the monster's health to: {mHealthPoints}")

    print("The monster strikes!!!")
    print(f"Monster's Claw ({mCombatStrength}) ---> You ({healthPoints})")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print(f"The monster has reduced your health to: {healthPoints}")

# --- Weapon Roll Logic
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
weaponRoll = random.randint(1, 6)  # Roll a random weapon

# Add weaponRoll to the hero's combat strength
combatStrength += weaponRoll
weapon = weapons[weaponRoll - 1]  # Use the rolled number to choose the weapon

# Print weapon details
print(f"Your weapon: {weapon}")

# Conditional message based on weaponRoll
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

# If weapon is not Fist
if weapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")