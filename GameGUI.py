import tkinter as tk
import boggle_board_randomizer
import ex12_utils

LETTER_HOVER_COLOR = "lightblue"
LETTER_REGULAR_COLOR = "lightgray"
BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'

BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tk.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}

class BoardGUI:

    _buttons = dict()

    def __init__(self, parent, board):
        parent.title("hobogobo game")
        self._outer_frame = tk.Frame(parent)
        self.__text_label = tk.Label(self._outer_frame, text = "A word", font = ("Courier", 30))
        self.__player_score = 0

        self._lower_frame = tk.Frame(self._outer_frame)
        self._letters_frame = tk.Frame(self._lower_frame)
        self.__start_button = tk.Button(self._letters_frame, text="Start Game!")
        self._create_buttons_in_lower_frame(board)

        self._artibute_frame = tk.Frame(self._lower_frame)
        self._clock = tk.Label(self._artibute_frame, text = "time",fg = "yellow",  bg = "black", font = ("Courier", 15))
        self._score = tk.Label(self._artibute_frame, text = "Score:" + str(self.__player_score) , font = ("Courier", 15))
        self._found_words = tk.Label(self._artibute_frame, text = "Found words: \n YOU \n ARE \n A \n Bitch", font = ("Courier", 15))


        self.pack()


    def _create_buttons_in_lower_frame(self, board) -> None:
        for i in range(5):
            tk.Grid.columnconfigure(self._letters_frame, i, weight=1)
        for i in range(4):
            tk.Grid.rowconfigure(self._letters_frame, i, weight=1)

        for i in range(4):
            for j in range(4):
                self._make_button(board[i][j], i, j)

    def _make_button(self, button_char, row, col, rowspan = 1, columnspan = 1):
        button = tk.Button(self._letters_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tk.NSEW)
        self._buttons[button_char] = button


        def _on_enter(event):
            button['background'] = LETTER_HOVER_COLOR

        def _on_leave(event):
            button['background'] = LETTER_REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)

        return button

    def pack(self):
        self._outer_frame.pack(fill=tk.BOTH, expand=True)
        self._lower_frame.pack(side = tk.BOTTOM)
        self._letters_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.__text_label.pack(side = tk.TOP)
        self._artibute_frame.pack(side = tk.RIGHT)
        self._clock.pack(fill = tk.X, side = tk.TOP)
        self._score.pack()
        self._found_words.pack()



if __name__ == '__main__':
    board = boggle_board_randomizer.randomize_board()
    root = tk.Tk()
    game_board = BoardGUI(root, board)
    root.mainloop()