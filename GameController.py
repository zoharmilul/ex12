import GameGUI as gui
import ex12_utils as utls
import boggle_board_randomizer as helper
import tkinter as tk

class GameController:

    def __init__(self, board, words_list):
        self.board = board
        self.gui = gui.BoardGUI(self.board)
        self.words = words_list
        self.path = []

        for button in self.gui._buttons:
            action = self.create_action(button, "letter")
            self.gui.set_button_command(button, action)

        action = self.create_action(self.gui._start_button, "start")
        self.gui.set_button_command(self.gui._start_button, action)

        action = self.create_action(self.gui._delete_button, "delete")
        self.gui.set_button_command(self.gui._delete_button, action)

        action = self.create_action(self.gui._delete_button, "enter")
        self.gui.set_button_command(self.gui._enter_button, action)


    def delete_letter(self):
        if len(self.path) > 0:
            self.path.pop()
        print(self.path)

    def update_path(self, cord):
        self.path.append(cord)
        print(self.path)

    def create_action(self, button, type):
        if type == "letter":

            def inner():
                if self.gui.game_is_on:
                    cord = self.gui.get_button_cord(button)
                    self.update_path(cord)
                    word = utls._get_word(self.board, self.path)
                    self.gui.update_text_label(word)
            return inner

        if type == "delete":

            def inner():
                if self.gui.game_is_on:
                    self.delete_letter()
                    if self.path:
                        word = utls._get_word(self.board, self.path)
                    else:
                        word = ""
                    self.gui.update_text_label(word)
            return inner

        if type == "start":

            def inner():
                self.gui.start_game()
            return inner

        if type == "enter":

            def inner():
                if self.gui.game_is_on:
                    print(utls.is_valid_path(self.board, self.path, self.words))
                    self.gui.pressed_enter()
                    word = utls.is_valid_path(self.board, self.path, self.words)
                    if word and word not in self.gui.found_words_text:
                        self.gui.update_words_label(word)
                        score = (len(word))**2
                        self.gui.set_score(score)
                    self.path = []
            return inner

    def start_game(self):
        self.gui._root.mainloop()


if __name__ == '__main__':
    board = helper.randomize_board()
    words_list = utls.load_words_dict("boggle_dict.txt")
    controller = GameController(board, words_list)
    print(controller.start_game())

