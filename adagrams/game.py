from random import randint

def letter_pool_as_list():
    """Creates a list of the available letters.

    Args:
        none
    
    Returns:
        list: letter_pool_list (list of strings). Each string is a single capital letter. The number of each capital letter depends on fluency as defined in LETTER_POOL.
    """
    LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 
    'E': 12, 'F': 2, 'G': 3, 'H': 2, 
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 
    'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 
    'X': 1, 'Y': 2, 'Z': 1
    }
    letter_pool_list = []
    for letter, frequency in LETTER_POOL.items():
        for _ in range(0, frequency): 
            letter_pool_list.append(letter)

    return letter_pool_list

def draw_letters():
    """Simulates drawing 10 tiles from a pile. Accounts for letter distribution.

    Args:
        None

    Returns:
        list: tiles (list of strings)
    """
    STARTING_LETTER_LIST = letter_pool_as_list()
    MAX_INDEX_LETTER_LIST = len(STARTING_LETTER_LIST) - 1
    tiles = []
    while len(tiles) < 10:
        random_index = randint(0, MAX_INDEX_LETTER_LIST)
        letter = STARTING_LETTER_LIST[random_index]

        if tiles.count(letter) < STARTING_LETTER_LIST.count(letter):
            tiles.append(letter)
        else:
            continue

    return tiles

def build_frequency_map(word):
    letter_frequency = {}
    for letter in word:
        letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
    return letter_frequency
    
def uses_available_letters(word, letter_bank):
    """Checks if a player-submitted word only uses letters from the player's letter bank.

    Args:
        word (str): The word submitted by the player.
        letter_bank (list): The list of letters the player has from drawing 10 tiles.

    Returns:
        bool: True if all letters in the submitted word are from letter pool. False if not. Will also return False if a letter's frequency in the word is greater than its frequency in the letter_bank.
    """
    capitalize_word = word.upper()
    word_letter_frequency = build_frequency_map(capitalize_word)
    letter_bank_frequency = build_frequency_map(letter_bank)
    for letter in capitalize_word:
        if letter not in letter_bank_frequency.keys() or word_letter_frequency[letter] > letter_bank_frequency[letter]:
            return False
        
    return True

def score_word(word):
    """Calculate the score for a word.

    Args:
        word (str): The word submitted by a player.

    Returns
        int: score of word based on scoring guidelines for each letter.
    """
    SCORE_CHART = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 
    'E': 1, 'F': 4, 'G': 2, 'H': 4, 
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 
    'M': 3, 'N': 1, 'O': 1, 'P': 3, 
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
    'U': 1, 'V': 4, 'W': 4, 
    'X': 8, 'Y': 4, 'Z': 10
    }
    score = 0
    if len(word) >= 7 and len(word) <= 10:
        score += 8
    
    for letter in word.upper():
        score += SCORE_CHART[letter]

    return score

def get_tied_words(word_list):
    """Finds maximum score from a list of words and returns a list of words with the same score.

    Args:
        word_list: List of strings representing words the player has submitted.
    
    Returns:
        words_tied_for_highest: List of strings representing words the player has submitted that tie for highest score.
    """
    highest_score = 0
    tied_words = []
    for word in word_list:
        if score_word(word) > highest_score:
            highest_score = score_word(word)

    for word in word_list:
        if score_word(word) == highest_score:
            tied_words.append(word)
    
    return tied_words

def get_highest_word_score(word_list):
    """Determines the highest scoring word from a list of words, accounting for all tie breaking conditions.

    Args:
        word_list (list): List of words the player has submitted.
    
    Returns:
        tuple: winning word, score of winning word.
    """
    tied_words = get_tied_words(word_list)

    if len(tied_words) == 1:
        return tied_words[0], score_word(tied_words[0])

    shortest_word = tied_words[0]
    for word in tied_words:
        if len(word) == 10:
            return word, score_word(word)
        else:
            if len(word) < len(shortest_word):
                shortest_word = word

    return shortest_word, score_word(shortest_word)