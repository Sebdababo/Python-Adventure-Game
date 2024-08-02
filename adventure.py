import random

inventory = []
player_health = 100
enemy_health = 50
game_over = False
score = 0

def start_game():
    print("Welcome to the Text Adventure!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Your adventure begins...")
    return player_name

def explore_room(player_name):
    print(f"{player_name}, you find yourself in a dimly lit room.")
    print("You see a door to the north and a window to the east.")
    while True:
        choice = input("What do you want to do? (north/east/inventory/status/quit): ").lower()
        if choice == "north":
            return explore_hallway
        elif choice == "east":
            return explore_garden
        elif choice == "inventory":
            show_inventory(player_name)
        elif choice == "status":
            show_status(player_name)
        elif choice == "quit":
            return None
        else:
            print("Invalid choice. Try again.")

def explore_hallway(player_name):
    print("You open the door and step into a hallway.")
    print("You see a staircase going up and a door to the west.")
    while True:
        choice = input("What do you want to do? (up/west/inventory/status/quit): ").lower()
        if choice == "up":
            return explore_second_floor
        elif choice == "west":
            return explore_library
        elif choice == "inventory":
            show_inventory(player_name)
        elif choice == "status":
            show_status(player_name)
        elif choice == "quit":
            return None
        else:
            print("Invalid choice. Try again.")

def explore_garden(player_name):
    global score
    print("You look out the window and see a beautiful garden.")
    if "mysterious key" not in inventory:
        print("You notice a key hidden among the flowers.")
        while True:
            choice = input("Do you want to get the key? (yes/no/inventory/status/quit): ").lower()
            if choice == "yes":
                print("You've obtained a mysterious key!")
                inventory.append("mysterious key")
                score += 10
                print(f"Your score increased by 10 points! Current score: {score}")
                break
            elif choice == "no":
                print("You decide to leave the key where it is.")
                break
            elif choice == "inventory":
                show_inventory(player_name)
            elif choice == "status":
                show_status(player_name)
            elif choice == "quit":
                return None
            else:
                print("Invalid choice. Try again.")
    else:
        print("The garden looks peaceful, but you've already taken the key.")
    return explore_room

def explore_second_floor(player_name):
    global score
    print("You climb the stairs to the second floor.")
    print("You see a locked door with a keyhole.")
    if "mysterious key" in inventory:
        while True:
            choice = input("Do you want to use the mysterious key? (yes/no/inventory/status/quit): ").lower()
            if choice == "yes":
                print("The key fits! You unlock the door and find a treasure chest!")
                score += 20
                print(f"Your score increased by 20 points! Current score: {score}")
                print("But wait! A monster appears and attacks you!")
                return battle
            elif choice == "no":
                print("You decide not to use the key.")
                break
            elif choice == "inventory":
                show_inventory(player_name)
            elif choice == "status":
                show_status(player_name)
            elif choice == "quit":
                return None
            else:
                print("Invalid choice. Try again.")
    else:
        print("The door is locked. You need to find a key.")
    return explore_hallway

def explore_library(player_name):
    global score
    print("You open the door and find a library.")
    print("There's a book on a pedestal that seems important.")
    while True:
        choice = input("Do you want to read the book? (yes/no/inventory/status/quit): ").lower()
        if choice == "yes":
            print("The book contains a clue: 'The key to your success lies in nature's embrace.'")
            score += 5
            print(f"Your score increased by 5 points! Current score: {score}")
            break
        elif choice == "no":
            print("You decide not to read the book.")
            break
        elif choice == "inventory":
            show_inventory(player_name)
        elif choice == "status":
            show_status(player_name)
        elif choice == "quit":
            return None
        else:
            print("Invalid choice. Try again.")
    return explore_hallway

def show_inventory(player_name):
    if inventory:
        print(f"{player_name}'s inventory: {', '.join(inventory)}")
    else:
        print(f"{player_name}'s inventory is empty.")

def show_status(player_name):
    print(f"{player_name}'s health: {player_health}")
    print(f"Current score: {score}")

def battle(player_name):
    global player_health, enemy_health, game_over, score
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
        score += 50
        print(f"Your final score: {score}")
        game_over = True
    else:
        print("Game over. The monster has defeated you.")
        print(f"Your final score: {score}")
        game_over = True
    return None

def main():
    player_name = start_game()
    current_location = explore_room
    while not game_over and current_location:
        current_location = current_location(player_name)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()