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

def create_leaderboard(word_list):
    leaderboard = {}

    for word in word_list:
        leaderboard[word] = score_word(word)

    return leaderboard

def check_for_all_way_tie(leaderboard):
    all_way_tie = False
    scores = list(leaderboard.values())

    for i in range(1, len(scores)):
        if scores[i - 1] == scores[i]:
            all_way_tie = True
    
    return all_way_tie

def check_for_all_same_length(leaderboard):
    all_same_length = False
    lengths = list(leaderboard.keys())

    for i in range(1, len(lengths)):
        if lengths[i - 1] == lengths[i]:
            return True
        
    return all_same_length

def get_highest_word_score(word_list):
    leaderboard = create_leaderboard(word_list)

    # Start at the first item of dictionary
    best_word = word_list[0]
    highest_score = leaderboard[best_word]

    all_way_tie = check_for_all_way_tie(leaderboard)
    all_same_length = check_for_all_same_length(leaderboard)

    if not all_way_tie and not all_same_length:
    # If all the scores are different and all the words are different lengths
        for current_word, score in leaderboard.items():
            if score > highest_score:
                best_word = current_word
                highest_score = score
            # Tie in score!
            # If the score is the same as current high score
            # and the current word is not the best word
            if score == highest_score and current_word != best_word:

                if len(best_word) > len(current_word) and len(best_word) != 10:
                # If the length of best word is greater than length
                # of current word, best_word gets replaced with current.
                # Unless the length of the current best word is 10, then it
                # will assign a new best word
                    best_word = current_word
                elif len(current_word) == 10:
                # Elif the length of the current word is 10, 
                # reassign it to best word
                    best_word = current_word

    if all_way_tie and not all_same_length:
    # If all the scores are the same and the lengths of words are different
        for current_word in leaderboard.keys():
            if best_word == current_word:
                continue
            if len(current_word) < len(best_word) and len(best_word) != 10:
                best_word = current_word
            elif len(best_word) == 10:
                break
    return best_word, highest_score