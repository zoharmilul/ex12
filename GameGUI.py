import tkinter as tk
import boggle_board_randomizer
import GameController as logic
import ex12_utils

LETTER_HOVER_COLOR = "lightblue"
LETTER_REGULAR_COLOR = "lightgray"
BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'skyblue'

BUTTON_STYLE = {"font": ("arial", 15),
                "borderwidth": 1,
                "relief": tk.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}

class BoardGUI:



    def __init__(self, parent, board):
        self.root = parent
        self._board = board
        self._word = "welcome"
        self._buttons = dict()

        self._outer_frame = tk.Frame(parent)
        self._text_label = tk.Label(self._outer_frame, text = self._word, font = ("arial", 30))
        self._delete_button = tk.Button(self._outer_frame, text = "Delete")

        self._lower_frame = tk.Frame(self._outer_frame)
        self._letters_frame = tk.Frame(self._lower_frame)
        self._start_button = tk.Button(self._letters_frame, text="Start Game!")

        self._arttibute_frame = tk.Frame(self._lower_frame)
        self._clock = tk.Label(self._arttibute_frame, text ="Press start to play", fg ="yellow", bg ="black", font = ("arial", 15))
        self._score = tk.Label(self._arttibute_frame, text ="Score: ", font = ("arial", 15))
        self._found_words = tk.Label(self._arttibute_frame, text ="Found words: \n YOU \n ARE \n A \n Bitch", font = ("arial", 15))
        self._enter_button = tk.Button(self._arttibute_frame, text ="Enter")

        self.pack()

    def start_game(self):
        self._word = ""
        self._text_label["text"] = self._word
        self._create_buttons_in_lower_frame(self._board)
        self.set_timer(180000)

    def set_timer(self, count):
        self._clock["text"] = str(int((count/(1000*60)) % 60)) + ":" + str(int((count/1000) % 60))
        if count > 0:
            self.root.after(1000, self.set_timer, count-1000)

    def letter_pressed(self, button):
        button["background"] = "skyblue"
        self._word += self._buttons[button][0]
        self._text_label["text"] = self._word

    def _create_buttons_in_lower_frame(self, board):
        for i in range(5):
            tk.Grid.columnconfigure(self._letters_frame, i, weight=1)
        for i in range(4):
            tk.Grid.rowconfigure(self._letters_frame, i, weight=1)

        for i in range(4):
            for j in range(4):
                self._make_button(board[i][j], i, j)

    def set_button_command(self,button,action):
        button.configure["command"] = action

    def get_button_cord(self, button):
        return self._buttons[button][1]

    def _make_button(self, button_char, row, col, rowspan = 1, columnspan = 1):
        self._start_button.pack_forget()
        button = tk.Button(self._letters_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tk.NSEW)
        self._buttons[button] = [button_char, (row, col)]

        def _on_enter(event):
            button['background'] = LETTER_HOVER_COLOR

        def _on_leave(event):
            button['background'] = LETTER_REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)

        return button

    def pack(self):
        self._outer_frame.pack(fill=tk.BOTH, expand=True)
        self._lower_frame.pack(side=tk.BOTTOM)
        self._start_button.pack(fill=tk.BOTH, expand=True)
        self._letters_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._text_label.pack(side=tk.TOP)
        self._arttibute_frame.pack(side=tk.RIGHT)
        self._clock.pack(fill=tk.X, side=tk.TOP)
        self._score.pack()
        self._found_words.pack()
        self._enter_button.pack(fill=tk.X)
        self._delete_button.pack(side = tk.RIGHT)

if __name__ == '__main__':
    board = boggle_board_randomizer.randomize_board()
    root = tk.Tk()
    game_board = BoardGUI(root, board)
    root.mainloop()