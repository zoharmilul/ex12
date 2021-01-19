import boggle_board_randomizer as helper
import time


def load_words_dict(file_path):
    word_dict = dict()
    with open(file_path, "r") as word_file:
        for line in word_file.readlines():
            word_dict[line.strip("\n")] = True
    return word_dict


def is_valid_path(board, path, words):
    if not path:
        return
    for i, coord in enumerate(path):
        if not check_valid_coords(coord, path):
            return
        if i < len(path) - 1:
            if not check_valid_step(path[i], path[i + 1]):
                return

    word = _get_word(board, path)
    if 3 <= len(word) <= 16 and word in words:
        return word


def find_length_n_words(n, board, words):
    valid_path = []
    words_list = set(filter(lambda x: len(x) == n, words.keys()))
    if not words_list:
        return []
    for i in range(len(board)):
        for j in range(len(board[0])):
            valid_path += _find_length_helepr(n, [(i, j)], board[i][j], [], board, words_list)
    return valid_path


def _find_length_helepr(n, curr_path, curr_word, paths, board, words_list):
    if len(curr_word) > n:
        return
    if len(curr_word) == n:
        if curr_word and check_curr_word(curr_word, words_list):
            paths.append((curr_word, curr_path))
        return paths

    if check_curr_word(curr_word, words_list):
        for step in get_valid_steps(curr_path[-1], curr_path):
            _find_length_helepr(n, curr_path + [step], curr_word + board[step[0]][step[1]], paths, board, words_list)
    return paths


def check_curr_word(curr_word, words_list):
    if curr_word:
        for word in words_list:
            if curr_word == word[:len(curr_word)]:
                return True
    return False


def check_valid_coords(coord, path):
    return 0 <= coord[0] <= 3 and 0 <= coord[1] <= 3 and path.count(coord) <= 1


def check_valid_step(coord1, coord2):
    return abs(coord1[0] - coord2[0]) <= 1 and abs(coord1[1] - coord2[1]) <= 1


def _get_word(board, path):
    word = ""
    for coord in path:
        word += board[coord[0]][coord[1]]
    return word


def get_valid_steps(cord, path):
    steps = [(cord[0] + 1, cord[1]), (cord[0] + 1, cord[1] + 1), (cord[0] + 1, cord[1] - 1),
                   (cord[0] - 1, cord[1]), (cord[0] - 1, cord[1] + 1), (cord[0] - 1, cord[1] - 1),
                   (cord[0], cord[1] + 1), (cord[0], cord[1] - 1)]
    final_steps = []
    for step in steps:
        if 0 <= step[0] <=3 and 0 <= step[1] <= 3 and path.count(step) == 0:
            final_steps.append(step)
    return final_steps


if __name__ == "__main__":
    board = helper.randomize_board()

    words = load_words_dict("boggle_dict.txt")
    for i in range(3, 17):
        print(i)
        start = time.time()
        print(find_length_n_words(i, board, words))
        end = time.time()
        print(end - start)
