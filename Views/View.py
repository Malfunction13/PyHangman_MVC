import re

class View:
    def __init__(self):
        self.hangman_graphic = """
        1 2 2 2 2 2 2 2
        1             3
        1             3
        1             4
        1           4 4 4
        1             4
        1           8 5 9
        1          8  5  9
        1           6   7
        1          6     7
        1 1
        1   1
        """

    def ask_name(self):
        name = input("Please insert your name: ")

        return name

    def greeting(self, name):
        print(f"Welcome, {name} Lets play a deadly game!")

    def announce_rules(self):
        print("You have to guess the word in 9 attempts or this poor man will hang!")

    def ask_guess(self):
        guess = input("Guess a letter: ").lower()

        return guess

    def separator(self):
        print("=" * 20)

    def hint(self, word):
        print(f"""The word you have to guess has {len(word)} letters and you have 9 lives left!
                    Let the hanging begin!""")

    def draw_hangman(self, lives):
        new_hangman = re.sub("[1-{}]".format(9-lives), "*", self.hangman_graphic)
        new_hangman = re.sub("[{}-9]".format(8-lives+2), " ", new_hangman)
        print(new_hangman)

    def display_hidden_word(self, hidden_word):
        print(*(i for i in hidden_word), sep=" ")

    def wrong_input(self):
        print("Please insert only 1 letter at a time from A-Z!")

    def already_guessed(self):
        print("Already guessed, try again!")

    def correct(self):
        print("YES! Your guess was CORRECT!")

    def wrong(self, lives):
        print(f"Sorry, your guess was WRONG :( You lose 1 life!\nYou have {lives} lives left.")

    def correct_list(self, correct_guesses):
        print("Correct guesses:", *correct_guesses)

    def wrong_list(self, wrong_guesses):
        print("Wrong letters:", *wrong_guesses)

    def win(self, word):
        print("YOU DID IT!\nYou win!!!")
        print(f"The word was {word.upper()}!")

    def loss(self, word):
        print("You loose, but the hanging man lost more! HA - HA - HAaaa!")
        print(f"The word was {word.upper()}!")

    def bye(self):
        print("Thank you for playing PyHangman!")
