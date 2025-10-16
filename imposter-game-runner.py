import random
import os

def clear_screen():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def get_num_players():
    while (True):
        n = input("Enter the number of players: ")
        if (n.isdigit()) and (int(n) > 0):
            break
        else:
            print("Invalid number of players. Do better.")
    clear_screen()
    return int(n)

def get_player_names(n):
    player_arr = []
    player_count = len(player_arr)
    while (player_count < n):
        name = input(f"Enter name of player {player_count + 1}: ")
        player_arr.append(name)
        player_count = len(player_arr)
    random.shuffle(player_arr)
    clear_screen()
    return player_arr

def get_player_roles(player_arr):
    imposter = random.choice(player_arr)
    chooser = random.choice(player_arr)
    while (chooser == imposter):
        chooser = random.choice(player_arr)
    return (imposter, chooser)

def get_secret_word(player_arr, chooser):
    print("The secret word will now be chosen. Each player will enter a word.\n\n")

    for player in player_arr:
        input(f"Pass the device to {player}.\nAll other players, avert thy gaze.\n\n\n{player}, press [enter] to continue...")

        while True:
            word = input("Enter a secret word: ")
            print(f"The current word is: {word}")
            yn = input("Do you want to keep the current word? Enter 'y' for yay or 'n' for nay: ").lower()

            if (yn == "y") or (yn == "yay") or (yn == "yes"):
                break
            elif (yn == "n") or (yn == "nay") or (yn == "no"):
                print("Choose a new secret word.")
            else:
                print("That wasn't one of the options...")

        if (player == chooser):
            secret_word = word

        clear_screen()

    return secret_word

def start_game(player_arr, imposter, secret_word):
    print("Players will now find out their role.\n\n")

    for player in player_arr:
        input(f"Pass the device to {player}.\nAll other players, avert thy gaze.\n\n\n{player}, press [enter] to continue...")

        if (player == imposter):
            input("You are the imposter.\nPress [enter] to continue...")
        else:
            input(f"You are not the imposter.\nThe secret word is: {secret_word}\nPress [enter] to continue...")

        clear_screen()


try:
    NUM_PLAYERS = get_num_players()
    PLAYERS = get_player_names(NUM_PLAYERS)
    IMPOSTER, CHOOSER = get_player_roles(PLAYERS)
    WORD = get_secret_word(PLAYERS, CHOOSER)
    start_game(PLAYERS, IMPOSTER, WORD)
except KeyboardInterrupt:
    print("\n\n\nGame ended.")
except Exception as e:
    print(f"Exception: {e}")
