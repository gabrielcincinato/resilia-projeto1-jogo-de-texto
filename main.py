from games import *
from custom_functions import *
from elements import *
from time import sleep


def play_game(game):
    """Jogue o jogo"""
    dramatic_print(demon)
    sleep(1)
    win = game()
    if not win:
        dramatic_line_print(death, sleeptime=0.1)
    else:
        dramatic_line_print(end, sleeptime=0.1)


# Print logo and sinopsis
dramatic_line_print(logo)
sleep(1)
dramatic_print(sinopsis)
sleep(2)
skip()

# Present Characters and give the player a choice
characters = f"""\nEscolha um dos três personagens:{nicobulus_description}{quintinus_description}\
    {romanus_description}"""
dramatic_print(characters)
choice = input("""
Selecione uma letra: """).lower()

# Play the game according to the choice
if choice == 'a':
    play_game(play_nicobulus_game)
elif choice == 'b':
    play_game(play_quintinus_game)
else:
    play_game(play_romanus_game)
