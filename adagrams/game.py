from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def letter_pool_as_list():
    letter_pool_list = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(0, frequency):
            letter_pool_list.append(letter)
    
    # print(letter_pool_list)
    return letter_pool_list

STARTING_LETTER_LIST = letter_pool_as_list()
MAX_INDEX_LETTER_LIST = len(STARTING_LETTER_LIST) - 1

def draw_letters():
    tiles = []

    while len(tiles) < 10:
        random_index = randint(0, MAX_INDEX_LETTER_LIST)
        letter = STARTING_LETTER_LIST[random_index]

        if tiles.count(letter) < LETTER_POOL[letter]:
            tiles.append(letter)

        else:
            continue

    return tiles

def uses_available_letters(word, letter_bank):
    capitalize_word = word.upper()
    for letter in capitalize_word:
        if letter not in letter_bank:
            return False
        else:
            if capitalize_word.count(letter) > letter_bank.count(letter):
                return False
    return True

def score_word(word):
    score = 0
    if len(word) >= 7:
        score += 8
    
    for letter in word.upper():
        score += SCORE_CHART[letter]

    return score

def get_highest_word_score(word_list):
    leaderboard = {}
    for word in word_list:
        leaderboard[word] = score_word(word)
    
    best_word = word_list[0]
    highest_score = leaderboard[best_word]

    for word, score in leaderboard.items():
        if score > highest_score:
            best_word = word
            highest_score = score
        # Tie in score!
        # If the score is the same as current high score
        # and the current word is not the best word
        if score == highest_score and word != best_word:

            if len(best_word) > len(word):
            # If the length of best word is greater than length
            # of current word, best_word gets replaced with current.
                best_word = word

    return best_word, highest_score