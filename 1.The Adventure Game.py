#Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":  # Changed "else" to "elif"
        print("You found a boat!")   # Changed "else action" to "elif action"
elif place == "cave":                 # Changed "elif" to "elif place"
    print("You find a hidden treasure!")

#Task 2: Setting the Scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You can see a path leading deeper into the cave.")
    elif action == "proceed in the dark":
        print("You stumble in the darkness and find nothing.")
    else:
        print("Invalid action. Please choose 'light a torch' or 'proceed in the dark'.")
else:
    print("Invalid place. Please choose 'forest' or 'cave'.")

#Task 3: Default Path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  # Skip the code block if action is invalid
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You can see a path leading deeper into the cave.")
    elif action == "proceed in the dark":
        print("You stumble in the darkness and find nothing.")
    else:
        print("Invalid action. Please choose 'light a torch' or 'proceed in the dark'.")
else:
    print("Invalid place. Please choose 'forest' or 'cave'.")