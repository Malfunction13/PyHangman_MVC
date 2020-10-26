"""Simple hangman game"""


class Controller:
    def __init__(self, board, view):
        self.board = board
        self.view = view
        self.guess = ""
        self.correct_guesses = []
        self.wrong_guesses = []
        self.winner = None

    def take_guess(self):
        self.guess = self.view.ask_guess()

    def validate_guess(self):
        while True:

            if len(self.guess) > 1 or not self.guess.isalpha():
                self.view.wrong_input()
                self.take_guess()

            else:

                return True

    def handle_guess(self):
        if self.validate_guess():

            while True:

                if self.guess in [*self.correct_guesses, *self.wrong_guesses]:

                    self.view.already_guessed()
                    self.take_guess()

                else:

                    break

            if self.guess in self.board.random_word.random_word:
                self.correct_guesses.append(self.guess)
                self.view.correct()

            else:
                self.board.player.lives -= 1
                self.wrong_guesses.append(self.guess)
                self.view.draw_hangman(self.board.player.lives)
                self.view.wrong(self.board.player.lives)

    def hidden_word(self):
        hidden_word = ""

        for letter in self.board.random_word.random_word:

            if letter in self.correct_guesses:
                hidden_word += letter

            else:
                hidden_word += "_"

        return hidden_word

    def check_winner(self):

        if self.hidden_word().strip() == self.board.random_word.random_word:
            self.view.win(self.board.random_word.random_word)
            self.winner = True

        if self.board.player.lives == 0:
            self.view.loss(self.board.random_word.random_word)
            self.winner = False

    def intro(self):
        self.view.greeting(self.board.player.name)
        self.view.announce_rules()
        self.view.separator()

    def hint(self):
        self.view.separator()
        self.view.hint(self.board.random_word.random_word)
        self.view.separator()
        self.view.display_hidden_word(self.hidden_word())

    def result(self):
        self.view.separator()
        self.view.display_hidden_word(self.hidden_word())
        self.view.correct_list(self.correct_guesses)
        self.view.wrong_list(self.wrong_guesses)

    def close(self):
        self.view.bye()
