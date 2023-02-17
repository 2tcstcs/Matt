"""
File: boggle.py
Name:Matt
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
SIZE = 4


def main():
    """
    TODO:
    """
    start = time.time()
    board = []
    while len(board) < SIZE:
        row = input(f'{len(board) + 1} row of letters: ').lower().split()    # 去除空隔把元素加至list
        if len(row) == SIZE:
            for i in row:
                if len(i) != 1 or not i.isalpha():
                    print('illegal input')
                    break  # 只會 break 當前迴圈
            board.append(row)
        else:
            print('illegal input')
    word_set = read_dictionary()
    boggle(board, word_set)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(board, words_set):
    ans_lst = []
    for x in range(SIZE):                                       # 看每行
        for y in range(SIZE):                                   # 看每個字
            boggle_helper(board, '', x, y, ans_lst, words_set)  # 字典裡有哪些以這些字為起點的字
    print(f'There are {len(ans_lst)} words in total')           # 總共找到的字數


def boggle_helper(board, string, x, y, ans_lst, words_set):
    letter = board[x][y]           # 先把自己記錄起來
    board[x][y] = ''               # 避免串到自己所以先清空 (也可以給他個list紀錄所有串過的index, 有串過就不再串)
    string += letter               # 把自己加進去
    # base case
    if len(string) >= SIZE:
        if string in words_set and string not in ans_lst:
            ans_lst.append(string)
            print(f'Found: {string}')

    # to find the longer answer
    x_y_lst = [(i, j) for i in range(x - 1, x + 2) if 0 <= i < SIZE
                   for j in range(y - 1, y + 2) if 0 <= j < SIZE if i != x or j != y]

    for new_x, new_y in x_y_lst:
        if board[new_x][new_y]:
            boggle_helper(board, string, new_x, new_y, ans_lst, words_set)

    board[x][y] = letter


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dictionary = []                   # 開空白 list
    with open(FILE, 'r') as f:        # 類字典但沒有index也沒有順序的資料結構
        words = f.read().split()      # 讀檔案裡的東西併用空白間隔開
        words_set = set(words)        # 把字都丟到set的資料裡
    return words_set


def neighbor_testing():                                # 把每個座標的鄰居變成 list
    for x in range(SIZE):
        for y in range(SIZE):
            x_y_lst = [(i, j) for i in range(x - 1, x + 2) if 0 <= i < SIZE
                       for j in range(y - 1, y + 2) if 0 <= j < SIZE if i != x or j != y]
            print(f'({x},{y} neighbor :{x_y_lst}')


def has_prefix(sub_s, s_dict):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in s_dict:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()



for pet,adj in d.items():
    count = 0
    for adj in adj_lst:
        if adj in adj_sst:
            count+=1
    if count = len(adj_lst):
        ans = ans + pet+','
    if ans:
        print(ans)
    else
        print("")