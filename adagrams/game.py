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
    """Creates a list of the available letters.

    Args:
        none
    
    Returns:
        list: letter_pool_list (list of strings)
    """
    letter_pool_list = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(0, frequency):
            letter_pool_list.append(letter)

    return letter_pool_list

STARTING_LETTER_LIST = letter_pool_as_list()
MAX_INDEX_LETTER_LIST = len(STARTING_LETTER_LIST) - 1

def draw_letters():
    """Simulates drawing 10 tiles from a pile. Accounts for letter distribution.

    Args:
        None

    Returns:
        list: tiles (list of strings)
    """
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
    """Checks if a word only uses letters from a player's letter bank.

    Args:
        word (str): The word submitted by the player.
        letter_bank (list): The list of letters the player has from drawing 10 tiles.

    Returns:
        bool: True if all letters are from letter pool selected. False if not.
    """
    capitalize_word = word.upper()
    for letter in capitalize_word:
        if letter not in letter_bank:
            return False
        else:
            if capitalize_word.count(letter) > letter_bank.count(letter):
                return False
    return True

def score_word(word):
    """Calculate the score for a word.

    Args:
        word (str): The word submitted by a player.

    Returns
        int: score of word based on scoring guidelines for each letter.
    """
    score = 0
    if len(word) >= 7:
        score += 8
    
    for letter in word.upper():
        score += SCORE_CHART[letter]

    return score

def create_leaderboard(word_list):
    """Creates a dictionary of words and their respective scores.

    Args:
        word_list (list): List of words submitted by player.

    Returns:
        dictionary: leaderboard, where keys are the words and their values are the scores.
    """
    leaderboard = {}

    for word in word_list:
        leaderboard[word] = score_word(word)

    return leaderboard

def find_maximum_score(scores):
    """Finds the maximum score in a list of scores.

    Args:
        scores (list): The list of scores a player has achieved.

    Returns
        int: highest_score. The maximum value in the list of scores.
    """
    highest_score = 0
    for score in scores:
        if score > highest_score:
            highest_score = score

    return highest_score

def check_for_high_score_tie(highest_score, scores):
    """Determines if there is a tie for highest score.

    Args:
        scores (list): A list of scores the player has achieved.

    Returns:
        bool: True if there is a tie for maximum score, False if the maximum score is a unique value.
    """
    if scores.count(highest_score) > 1:
        return True
    else:
        return False

def check_for_all_same_length(word_list):
    """Determines if words are the same length. Use only if there is a tie for highest score.

    Args:
        words (list): A list of words submitted by the player.

    Returns:
        bool: True if the highest score word has same length as other words it is tied with for highest score.
    """
    lengths = []

    for word in word_list:
        lengths.append(len(word))

    if lengths.count(lengths[0]) == len(lengths):
        return True
    
    return False

def check_for_ten_letter_word(word_list):
    """Determines if there is a ten letter word in the list of words.

    Args:
        words (list): A list of words submitted by the player.

    Returns:
        bool: True if there is at least one ten letter word, False if no ten letter words exist in the list.
    """
    for word in word_list:
        if len(word) == 10:
            return True
        
    return False

def find_first_ten_letter_word(word_list):
    """When there is a tie among scores and multiple ten letter words that are tied for first, selects the first ten letter word from the word_list.

    Args:
        word_list
    
    Returns:
        str: word. Returns the first word in the list that has a length of 10 letters.
    """
    for word in word_list:
        if len(word) == 10:
            return word

def get_shortest_word(word_list):
    """Determining the shortest word in the list of words.

    Args:
        word_list (list): List of words the player has submitted.
    
    Returns
        str: shortest_word. The string with the shortest length in the word_list.
    """

    shortest_word = word_list[0]
    for word in word_list:
        if len(word) < len(shortest_word):
            shortest_word = word

    return shortest_word

def get_tied_words(highest_score, leaderboard):
    """Creates a list of the words that are tied for highest score.

    Args:
        highest_score (int): The score the words have in common
        leaderboard (dict): Finds the words (keys) that have a score (value) of the highest score.

    Returns:
        list: tied_words. A list of all the words that have the same score and the score is the maximum score.
    """
    tied_words = []

    for word in leaderboard.keys():
        if leaderboard[word] == highest_score:
            tied_words.append(word)

    return tied_words

def get_highest_word_score(word_list):
    """Determines the highest scoring word from a list of words, accounting for all tie breaking conditions.

    Args:
        word_list (list): List of words the player has submitted.
    
    Returns:
        tuple: best_word, leaderboard[best_word] (score). Finds best_word key in the leaderboard and returns the key and its value.
    """
    leaderboard = create_leaderboard(word_list)
    scores = list(leaderboard.values())
    highest_score = find_maximum_score(scores)

    tie_for_highest_score = check_for_high_score_tie(highest_score, scores)

    if not tie_for_highest_score:
        for word, score in leaderboard.items():
            if score == highest_score:
                best_word = word
    
    else:
        tied_words = get_tied_words(highest_score, leaderboard)

        ten_letter_word_in_tie = check_for_ten_letter_word(tied_words)
        all_same_length = check_for_all_same_length(tied_words)

        if ten_letter_word_in_tie:
            best_word = find_first_ten_letter_word(tied_words)

        elif not ten_letter_word_in_tie and all_same_length:
            best_word = tied_words[0]

        else:
            best_word = get_shortest_word(tied_words)

    return best_word, leaderboard[best_word]