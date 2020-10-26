from Repository.JsonWords import JsonWords
from Models.Player import Player
from Models.RandomWord import RandomWord
from Models.Board import Board
from Views.View import View
from Controllers.Controller import Controller
from random import choice

player = Player(View().ask_name())
View().announce_rules()


def main():
    word = RandomWord(choice(JsonWords().get_words()))

    while "-" in word.random_word or " " in word.random_word:  # avoids words like "water-based" or entries with spaces
        word = RandomWord(choice(JsonWords().get_words()))

    board = Board(player, word)
    view = View()
    controller = Controller(board, view)

    controller.hint()

    while True:
        controller.take_guess()
        controller.handle_guess()
        controller.result()
        controller.check_winner()

        if controller.winner is not None:
            if play_again():
                main()

            else:
                controller.close()
                quit()


def play_again():
    """Asks user input until Y or N. Returns True/False, in case of wrong input notifies user and loops again."""

    while True:
        restart = input("Would you like to go for another round?\nInsert Y for YES and N for NO: ")

        if restart.lower() == "y":

            return True

        elif restart.lower() == "n":

            return False

        else:
            print("Wrong input!")


main()
