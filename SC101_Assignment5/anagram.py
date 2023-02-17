"""
File: anagram.py
Name:matt
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
words =[]
new_s= ''
sear_lst =[]


def main():
    global sear_lst

    ####################
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = str(input('Find anagram for: '))

        if s == EXIT:
            break
        else:
            find_anagrams(s)
            sear_lst = []   #印出結果後清空

    ####################



def read_dictionary():
    global words
    with open('dictionary.txt', 'r') as f:
        for word in f:
            words += word.split()


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    fund_lst =[]
    start = time.time()
    print('Searching...')
    find_anagrams_helper(s, new_s, [], len(s))

    #print(sear_lst)

    for i in range(len(sear_lst)):
        if sear_lst[i] in words:
            print('Found: ' + sear_lst[i])
            print('Searching...')
            fund_lst.append(sear_lst[i])
    print(f'{len(fund_lst)} anagrams for: {fund_lst}')
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def find_anagrams_helper(s, new_s, sear_word, ans_len):
    if len(new_s) == len(s):
        if new_s not in sear_lst:
            sear_lst.append(new_s)
    else:
        for i in range(len(s)):
            if has_prefix(new_s) is True:
                if new_s.count(s[i]) == s.count(s[i]):
                    pass
                else:
                    find_anagrams_helper(s, new_s+s[i], sear_word, ans_len) #讓每個字母跑recursion


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for sub_s in words:
        if sub_s.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
