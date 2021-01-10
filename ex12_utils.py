import boggle_board_randomizer as helper
import time

def load_words_dict(file_path):
    word_dict = dict()
    with open(file_path, "r") as word_file:
        for line in word_file.readlines():
            word_dict[line.strip("\n")] = True
    return word_dict


def is_valid_path(board, path, words):
    for i, coord in enumerate(path):
        if not check_valid_coords(coord, path):
            return
        if i != len(path) - 1 and check_valid_step(path[i], path[i + 1]):
            continue
        else:
            return

    word = _get_word(board, path)
    if word in words:
        return word


def find_length_n_words(n, board, words):
    valid_path = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            valid_path += _find_length_helepr(n, [(i, j)], [], board, words)

    print(valid_path)

def _find_length_helepr(n, curr_path, pathes, board, words):
    if len(curr_path) == n:
        pathes.append((_get_word(board,curr_path), curr_path[:]))
        return curr_path
    for step in get_valid_steps(curr_path[-1]):
        if check_curr_path(n, curr_path + [step], board, words):
            _find_length_helepr(n, curr_path + [step], pathes, board, words)

    return pathes


def check_curr_path(n, curr_path, board, words):
    words_list = list(filter(lambda x: len(x) == n, list(words.keys())))
    semi_word = _get_word(board, curr_path)
    if semi_word:
        for word in words_list:
            if semi_word == word[:len(semi_word)]:
                return True
    return False


def check_valid_coords(coord, path):
    return 0 <= coord[0] <= 3 and 0 <= coord[1] <= 3 and path.count(coord) == 1


def check_valid_step(coord1, coord2):
    return abs(coord1[0] - coord2[0]) <= 1 and abs(coord1[1] - coord2[1]) <= 1


def _get_word(board, path):
    word = ""
    if check_valid_coords(path[-1], path):
        for coord in path:
            word += board[coord[0]][coord[1]]
        return word


def get_valid_steps(cord):
    steps = [(cord[0] + 1, cord[1]), (cord[0] + 1, cord[1] + 1), (cord[0] + 1, cord[1] -1),
                   (cord[0] - 1, cord[1]), (cord[0] - 1, cord[1] + 1), (cord[0] - 1, cord[1] -1),
                   (cord[0], cord[1] + 1), (cord[0], cord[1] - 1)]

    valid_steps = list(filter(lambda x: check_valid_coords(x, [x]), steps))
    return valid_steps

board = helper.randomize_board()
words = load_words_dict("boggle_dict.txt")
start = time.time()
find_length_n_words(3, board, words)
end = time.time()
print(end-start)

# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0], curr_path[-1][1] + 1)], pathes,board, words)
# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0], curr_path[-1][1] - 1)], pathes,board, words)
# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0] + 1, curr_path[-1][1])], pathes,board, words)
# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0] - 1, curr_path[-1][1])], pathes,board, words)
# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0] - 1, curr_path[-1][1] + 1)], pathes,board, words)
# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0] - 1, curr_path[-1][1] - 1)], pathes,board, words)
# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0] + 1, curr_path[-1][1] + 1)], pathes,board, words)
# if check_curr_path(n,curr_path,board, words):
#     _find_length_helepr(n, curr_path + [(curr_path[-1][0] + 1, curr_path[-1][1] - 1)], pathes,board, words)