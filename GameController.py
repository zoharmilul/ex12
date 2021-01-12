import GameGUI as gui
import ex12_utils as utls
class GameController:

    def __init__(self):
        self.root = ""
        self.board = ""
        self.gui = gui.BoardGUI(self.root, self.board)
        self.logic = utls.GameLogic()
        self.path = []

        for button in self.gui._buttons:
            action = self.create_action(button, "letter")
            self.gui.set_button_command(button, action)

        action =self.create_action(self.gui._start_button,"start")
        self.gui.set_button_command(self.gui._start_button,action )

        action = self.create_action(self.gui._delete_button,"delete")
        self.gui.set_button_command(self.gui._delete_button, action)

    def delete_letter(self):
        self.path.pop()
        print(self.path)


    def create_action(self, button, type):
        if type == "letter":
            def inner():

                self.gui.letter_pressed(button)
                self.logic.update_path(self.gui.get_button_cord(button))

            return inner
        if type == "delete":

            def inner():
                # make delete functions
            return inner

        if type == "start":

            return self.gui.start_game

        if type == "enter":
            pass





