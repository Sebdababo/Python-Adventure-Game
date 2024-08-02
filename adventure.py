def start_game():
    print("Welcome to the Text Adventure!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Your adventure begins...")
    return player_name

def explore_room(player_name):
    print(f"{player_name}, you find yourself in a dimly lit room.")
    print("You see a door to the north and a window to the east.")
    choice = input("What do you want to do? (north/east): ").lower()
    if choice == "north":
        explore_hallway(player_name)
    elif choice == "east":
        explore_garden(player_name)
    else:
        print("Invalid choice. You remain in the room.")
        explore_room(player_name)

def explore_hallway(player_name):
    print("You open the door and step into a hallway.")
    print("You see a staircase going up and a door to the west.")
    choice = input("What do you want to do? (up/west): ").lower()
    if choice == "up":
        print("You climb the stairs to the second floor.")
    elif choice == "west":
        print("You open the door and find a library.")
    else:
        print("Invalid choice. You remain in the hallway.")
        explore_hallway(player_name)

def explore_garden(player_name):
    print("You look out the window and see a beautiful garden.")
    print("You notice a key hidden among the flowers.")
    choice = input("Do you want to get the key? (yes/no): ").lower()
    if choice == "yes":
        print("You've obtained a mysterious key!")
    elif choice == "no":
        print("You decide to leave the key where it is.")
    else:
        print("Invalid choice. You remain by the window.")
        explore_garden(player_name)

def main():
    player_name = start_game()
    explore_room(player_name)

if __name__ == "__main__":
    main()