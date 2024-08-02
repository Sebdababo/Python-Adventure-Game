import random

inventory = []
player_health = 100
enemy_health = 50

def start_game():
    print("Welcome to the Text Adventure!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Your adventure begins...")
    return player_name

def explore_room(player_name):
    print(f"{player_name}, you find yourself in a dimly lit room.")
    print("You see a door to the north and a window to the east.")
    choice = input("What do you want to do? (north/east/inventory/status): ").lower()
    if choice == "north":
        explore_hallway(player_name)
    elif choice == "east":
        explore_garden(player_name)
    elif choice == "inventory":
        show_inventory(player_name)
        explore_room(player_name)
    elif choice == "status":
        show_status(player_name)
        explore_room(player_name)
    else:
        print("Invalid choice. You remain in the room.")
        explore_room(player_name)

def explore_hallway(player_name):
    print("You open the door and step into a hallway.")
    print("You see a staircase going up and a door to the west.")
    choice = input("What do you want to do? (up/west/inventory/status): ").lower()
    if choice == "up":
        explore_second_floor(player_name)
    elif choice == "west":
        explore_library(player_name)
    elif choice == "inventory":
        show_inventory(player_name)
        explore_hallway(player_name)
    elif choice == "status":
        show_status(player_name)
        explore_hallway(player_name)
    else:
        print("Invalid choice. You remain in the hallway.")
        explore_hallway(player_name)

def explore_garden(player_name):
    print("You look out the window and see a beautiful garden.")
    print("You notice a key hidden among the flowers.")
    choice = input("Do you want to get the key? (yes/no/inventory/status): ").lower()
    if choice == "yes":
        print("You've obtained a mysterious key!")
        inventory.append("mysterious key")
    elif choice == "no":
        print("You decide to leave the key where it is.")
    elif choice == "inventory":
        show_inventory(player_name)
        explore_garden(player_name)
    elif choice == "status":
        show_status(player_name)
        explore_garden(player_name)
    else:
        print("Invalid choice. You remain by the window.")
        explore_garden(player_name)
    explore_room(player_name)

def explore_second_floor(player_name):
    print("You climb the stairs to the second floor.")
    print("You see a locked door with a keyhole.")
    if "mysterious key" in inventory:
        choice = input("Do you want to use the mysterious key? (yes/no/inventory/status): ").lower()
        if choice == "yes":
            print("The key fits! You unlock the door and find a treasure chest!")
            print("But wait! A monster appears and attacks you!")
            battle(player_name)
        elif choice == "no":
            print("You decide not to use the key.")
        elif choice == "inventory":
            show_inventory(player_name)
            explore_second_floor(player_name)
        elif choice == "status":
            show_status(player_name)
            explore_second_floor(player_name)
        else:
            print("Invalid choice. You remain on the second floor.")
            explore_second_floor(player_name)
    else:
        print("The door is locked. You need to find a key.")
    explore_hallway(player_name)

def explore_library(player_name):
    print("You open the door and find a library.")
    print("There's a book on a pedestal that seems important.")
    choice = input("Do you want to read the book? (yes/no/inventory/status): ").lower()
    if choice == "yes":
        print("The book contains a clue: 'The key to your success lies in nature's embrace.'")
    elif choice == "no":
        print("You decide not to read the book.")
    elif choice == "inventory":
        show_inventory(player_name)
        explore_library(player_name)
    elif choice == "status":
        show_status(player_name)
        explore_library(player_name)
    else:
        print("Invalid choice. You remain in the library.")
        explore_library(player_name)
    explore_hallway(player_name)

def show_inventory(player_name):
    if inventory:
        print(f"{player_name}'s inventory: {', '.join(inventory)}")
    else:
        print(f"{player_name}'s inventory is empty.")

def show_status(player_name):
    print(f"{player_name}'s health: {player_health}")

def battle(player_name):
    global player_health, enemy_health
    print("A battle begins!")
    while player_health > 0 and enemy_health > 0:
        print(f"Your health: {player_health} | Enemy health: {enemy_health}")
        choice = input("Do you want to attack or defend? ").lower()
        if choice == "attack":
            damage = random.randint(10, 20)
            enemy_health -= damage
            print(f"You deal {damage} damage to the enemy!")
        elif choice == "defend":
            print("You brace yourself for the enemy's attack.")
        else:
            print("Invalid choice. You lose your turn.")
        
        if enemy_health > 0:
            enemy_damage = random.randint(5, 15)
            if choice == "defend":
                enemy_damage //= 2
            player_health -= enemy_damage
            print(f"The enemy deals {enemy_damage} damage to you!")
    
    if player_health > 0:
        print("Congratulations! You've defeated the monster and won the game!")
    else:
        print("Game over. The monster has defeated you.")

def main():
    player_name = start_game()
    explore_room(player_name)

if __name__ == "__main__":
    main()