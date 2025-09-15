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
    words = list(leaderboard.keys())
    lengths = []

    for word in words:
        lengths.append(len(word))

    if lengths.count(lengths[0]) == len(lengths):
        return True
    
    return False

def highest_score_no_ties(scores):
    highest_score = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]

    return highest_score

def check_for_ten_letter_word(words):
    for word in words:
        if len(word) == 10:
            return True
        
    return False

def highest_score_depends_on_word_length(words):
    best_word = words[0]

    ten_letter_word_present = check_for_ten_letter_word(words)

    for word in words:
        if word == best_word:
            continue

        elif len(word) < len(best_word) and not ten_letter_word_present:
            best_word = word

        elif ten_letter_word_present:
            for word in words:
                if len(word) == 10:
                    best_word = word

    return best_word

def find_first_ten_letter_word(word_list):
    for word in word_list:
        if len(word) == 10:
            return word
        
def get_shortest_word(word_list):

    shortest_word = "AAAAAAAAAA"
    for word in word_list:
        if len(word) < len(shortest_word):
            shortest_word = word

    return shortest_word

def get_highest_word_score(word_list):
    leaderboard = create_leaderboard(word_list)
    scores = list(leaderboard.values())

    best_word = word_list[0]
    highest_score = scores[0]

    all_way_tie = check_for_all_way_tie(leaderboard)
    words_same_length = check_for_all_same_length(leaderboard)
    ten_letter_word_present = check_for_ten_letter_word(word_list)

    if (not all_way_tie) and (not words_same_length):
        highest_score = highest_score_no_ties(scores)
        index_highest_score = scores.index(highest_score)
        best_word = word_list[index_highest_score]

    elif (all_way_tie):
        if words_same_length and ten_letter_word_present:
            best_word = word_list[0]

        elif not words_same_length and ten_letter_word_present:
            best_word = find_first_ten_letter_word(word_list)

        elif not words_same_length and not ten_letter_word_present:
            best_word = get_shortest_word(word_list)

    return best_word, leaderboard[best_word]