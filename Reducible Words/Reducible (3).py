#  File: Reducible.py

#  Description: Program that finds the longest reducible word.

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created:10/23/19

#  Date Last Modified: 10/28/19


def main():
    # takes as input a positive integer n
    # returns True if n is prime and False otherwise
    def is_prime ( n ):
        if (n == 1):
            return False
        limit = int (n ** 0.5) + 1
        div = 2
        while (div < limit):
            if (n % div == 0):
                return False
            div += 1
        return True

    # takes as input a string in lower case and the size
    # of the hash table and returns the index the string
    # will hash into
    def hash_word (s, size):
        hash_idx = 0
        for j in range (len(s)):
            letter = ord (s[j]) - 96
            hash_idx = (hash_idx * 26 + letter) % size
        return hash_idx

    # takes as input a string in lower case and the constant
    # for double hashing and returns the step size for that
    # string
    def step_size (s, const):
        key = 0
        for j in range (len(s)):
            letter = ord (s[j]) - 96
            key += letter * 26 ** (len(s) - j - 1)

        return const - (key%const)

    # takes as input a string and a hash table and enters
    # the string in the hash table, it resolves collisions
    # by double hashing
    def insert_word(s, hash_table):
        step = step_size(s, 13)
        hash_size = n
        hash_idx = hash_word(s, hash_size)

        while hash_table[hash_idx] != '':
            if hash_idx + step < hash_size:
                hash_idx += step
            else:
                hash_idx += step
                hash_idx %= hash_size

            if hash_table[hash_idx] == '':
                break

        hash_table[hash_idx] = s

    # takes as input a string and a hash table and enters
    # the string in the hash table, it resolves collisions
    # by double hashing
    def helper_insert_word(s, hash_table):
        step = step_size(s, 13)
        hash_size = m
        hash_idx = hash_word(s, hash_size)

        while hash_table[hash_idx] != '':
            if hash_idx + step < hash_size:
                hash_idx += step
            else:
                hash_idx += step
                hash_idx %= hash_size

            if hash_table[hash_idx] == '':
                break

        hash_table[hash_idx] = s

    # takes as input a string and a hash table and returns True
    # if the string is in the hash table and False otherwise
    def find_word (s, hash_table):
        loops = 0
        step = step_size(s, 13)
        hash_size = n
        hash_idx = hash_word(s, hash_size)
        first_idx = hash_idx

        while hash_table[hash_idx] != s:
            if hash_table[hash_idx] == '':
                return False

            if hash_idx + step < hash_size:
                hash_idx += step
            else:
                hash_idx += step
                hash_idx %= hash_size
                loops += 1

            if loops > 1 and first_idx < hash_idx:
                return False

        if hash_table[hash_idx] == s:
            return True

        return False

    # takes as input a string and a hash table and returns True
    # if the string is in the hash table and False otherwise
    def helper_find_word (s, hash_table):
        loops = 0
        step = step_size(s, 13)
        hash_size = m
        hash_idx = hash_word(s, hash_size)
        first_idx = hash_idx


        while hash_table[hash_idx] != s:
            if hash_table[hash_idx] == '':
                return False

            if hash_idx + step < hash_size:
                hash_idx += step
            else:
                hash_idx += step
                hash_idx %= hash_size
                loops += 1

            if loops > 1 and first_idx < hash_idx:
                return False

        if hash_table[hash_idx] == s:
            return True

        return False

    # recursively finds if a word is reducible, if the word is
    # reducible it enters it into the hash memo and returns True
    # and False otherwise
    def is_reducible (s, hash_table, hash_memo):
        original_word = hashed_item
        s_copy = s[:]
        if len(s_copy) == 1:
            if (s_copy == 'a') or (s_copy == 'i') or (s_copy == 'o'):
                helper_insert_word(original_word, hash_memo)
                return True

        elif helper_find_word(s_copy, hash_memo):
            return True

        else:
            for i in range(len(s)):
                s_copy = s[:i] + s[i+1:]
                if find_word(s_copy, hash_table):
                    return is_reducible(s_copy, hash_table, hash_memo)
                else:
                    if len(s_copy) == 1:
                        if (s_copy == 'a') or (s_copy == 'i') or (s_copy == 'o'):
                            return True
            return False

    # goes through a list of words and returns a list of words
    # that have the maximum length
    def get_longest_words (string_list):
        # find all words with maximum length
        reduced_list = []

        max_len = 0
        for string in string_list:
            if len(string) > max_len:
                max_len = len(string)

        for string in string_list:
            if len(string) == max_len:
                reduced_list.append(string)
        return reduced_list

    # create an empty word_list
    word_list = []
    # open the file words.txt
    in_file = open("words.txt", "r")

    # read words from words.txt and append to word_list
    for word in in_file:
        word = word.strip()
        word_list.append(word)

    # close file words.txt
    in_file.close()

    # find length of word_list
    size = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    n = (2 * size) + 1
    while not is_prime(n):
        n = n + 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for x in range(n):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)

    # create an empty hash_memo
    hash_memo = []

    # populate the hash_memo with M blank strings
    m = 27000
    while not is_prime(m):
        m += 1

    for x in range(m):
        hash_memo.append('')

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for hashed_item in hash_list:
        if is_reducible(hashed_item, hash_list, hash_memo):
            # print(hashed_item)
            reducible_words.append(hashed_item)

    # find words of the maximum length in reducible_words
    reduced_list = []
    longest_reducible_words = get_longest_words(reducible_words)
    # print(get_longest_words(reducible_words))

    # print the words of maximum length in alphabetical order
    # one word per line
    alphabetical_reducible = sorted(longest_reducible_words)
    for word in alphabetical_reducible:
        print(word)
main()

