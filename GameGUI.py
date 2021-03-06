import tkinter as tk
from tkinter import messagebox
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

    def __init__(self, board):
        self._root = tk.Tk()
        self._root.title("Best game everrrrr by your favorite students")
        self._root.geometry("540x450")
        self._board = board
        self.game_is_on = False
        self._play_again = False
        self._word = "welcome"
        self._buttons = dict()
        self._score_value = 0
        self._outer_frame = tk.Frame(self._root)
        self._text_label = tk.Label(self._outer_frame, text=self._word, font=("arial", 30))
        self._delete_button = tk.Button(self._outer_frame, text="Delete")
        self._lower_frame = tk.Frame(self._outer_frame)
        self._letters_frame = tk.Frame(self._lower_frame)
        self._start_button = tk.Button(self._outer_frame, text="Start Game!")

        self._arttibute_frame = tk.Frame(self._lower_frame)
        self._clock = tk.Label(self._arttibute_frame, text="Press start to play", fg="yellow", bg="black",
                               font=("arial", 12))
        self._score_label = tk.Label(self._arttibute_frame, text="Score: " + str(self._score_value), font=('arial', 15))
        self._found_words_label = tk.Label(self._arttibute_frame, text="Found words: ",
                                           font=("arial", 10))
        self.words_scrollbar = tk.Scrollbar(self._arttibute_frame)  # todo
        self.scroll_text = tk.Listbox(self._arttibute_frame, yscrollcommand=self.words_scrollbar.set)
        self.words_scrollbar.config(command=self.scroll_text.yview)
        self._enter_button = tk.Button(self._arttibute_frame, text="Enter")
        self._create_buttons_in_lower_frame(self._board)
        self.pack()

    def start_game(self):
        self.game_is_on = True
        self._start_button.pack_forget()
        self.update_text_label("")
        self.set_timer(180000)
        self.set_button_text()

    def set_timer(self, count):

        # Update the timer in the game

        self._clock["text"] = str(int((count / (1000 * 60)) % 60)) + ":" + str(int((count / 1000) % 60))
        if count == 30000:
            for button in self._buttons:
                button["text"] = "?"
            messagebox.showinfo("Time is running out", "You have 30 seconds left!")
            self.set_button_text()
        if count > 0:
            self._root.after(1000, self.set_timer, count - 1000)
        if count == 0:
            if messagebox.askyesno("Time is up!!!!!!!!!", f"Your score is: {self._score_value} \n "
                                                          f"Do you want to play again?"):
                self._play_again = True
            self._root.destroy()

    def set_button_text(self):
        # Change the texts on the buttons
        for button in self._buttons:
            cord = self.get_button_cord(button)
            button["text"] = self._board[cord[0]][cord[1]]

    def _create_buttons_in_lower_frame(self, board):
        for i in range(5):
            tk.Grid.columnconfigure(self._letters_frame, i, weight=1)
        for i in range(4):
            tk.Grid.rowconfigure(self._letters_frame, i, weight=1)

        for i in range(4):
            for j in range(4):
                self._make_button(board[i][j], i, j)

    def update_text_label(self, word):
        self._word = word
        self._text_label["text"] = self._word

    def update_words_label(self, word):
        self.scroll_text.insert(tk.END, word)

    def set_button_command(self, button, action):
        button.configure(command=action)

    def get_button_cord(self, button):
        return self._buttons[button][1]

    def _make_button(self, button_char, row, col, rowspan=1, columnspan=1):
        button = tk.Button(self._letters_frame, text="?", **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tk.NSEW)
        self._buttons[button] = [button_char, (row, col)]

        def _on_enter(event):
            button['background'] = LETTER_HOVER_COLOR

        def _on_leave(event):
            button['background'] = LETTER_REGULAR_COLOR

        def _on_click(event):
            button["background"] = BUTTON_ACTIVE_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        button.bind("<Button-1>", _on_click)

        return button

    def set_score(self, score):
        self._score_value += score
        self._score_label["text"] = "Score: " + str(self._score_value)

    def pressed_enter(self):
        self.update_text_label("")


    def pack(self):
        self._outer_frame.pack(fill=tk.BOTH, expand=True)
        self._lower_frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        self._start_button.pack(fill=tk.BOTH, expand=True)
        self._letters_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._text_label.pack(side=tk.TOP)
        self._arttibute_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self._clock.pack(fill=tk.X, side=tk.TOP)
        self._score_label.pack()
        self._found_words_label.pack()
        self.words_scrollbar.pack(side=tk.RIGHT, fill=tk.Y) #todo
        self.scroll_text.pack()
        self._enter_button.pack(fill=tk.X)
        self._delete_button.pack(side=tk.RIGHT)
