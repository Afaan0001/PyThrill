import time

def introduction():
    print("Welcome to PyCraft: A Python-based Thriller Text Adventure Game!")
    time.sleep(1)
    print("You wake up in a dark alley, disoriented and surrounded by a thick fog.")
    time.sleep(1)
    print("Your heart is pounding, and you feel a sense of imminent danger.")
    time.sleep(1)
    print("Your mysterious journey begins now...\n")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def dark_alley_scenario():
    print("You navigate through the dark alley, the silence broken only by distant footsteps.")
    time.sleep(1)
    print("Suddenly, you hear a whisper, 'They're watching you.'")
    time.sleep(1)

    choices = ["Quickly move towards the source of the whisper.", "Stay in the shadows."]
    choice = make_choice(choices)

    if choice == 1:
        print("As you approach, you find a hidden entrance to an underground facility.")
        time.sleep(1)
        print("You've discovered a secret society. Be cautious; your choices will determine your fate.")
    else:
        print("You decide to stay in the shadows. The footsteps fade away, but the alley remains mysterious.")

def abandoned_building_scenario():
    print("You enter an abandoned building, the air thick with suspense.")
    time.sleep(1)
    print("A flickering light reveals a figure in the distance.")
    time.sleep(1)

    choices = ["Approach the figure cautiously.", "Find another way out of the building."]
    choice = make_choice(choices)

    if choice == 1:
        print("You approach the figure and realize it's a person in distress.")
        time.sleep(1)
        print("They warn you of impending danger. Your choices will determine your survival.")
    else:
        print("You decide to find another way out. The building is a maze of uncertainty, but you navigate it skillfully.")

def main():
    introduction()

    choices = ["Navigate through the dark alley.", "Enter the abandoned building."]
    choice = make_choice(choices)

    if choice == 1:
        dark_alley_scenario()
    else:
        abandoned_building_scenario()

    print("\nThanks for experiencing the thrilling adventure of PyCraft!")

if __name__ == "__main__":
    main()
