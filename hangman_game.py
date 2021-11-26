import ASCII_ART

HANGMAN_ASCII_ART = print("Welcome to the game Hangman")

print("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")

path = input('Please enter file path that contain random words: ')
index_of_word = int(input('Good! now enter number between 0-16: '))

# file_words_path = r'C:\Users\Naor\Desktop\words.txt'

# Function to choose a random word from txt file

def choose_word(file_path, index):

    f = open(file_path, 'r')
    f_read = f.readlines()

    result = []

    for word in f_read:
        result.append(word.split(','))

    word_by_index = result[0][index]

    return word_by_index

print("""
    x-------x
""")

secret_word = choose_word(path, index_of_word)
print('The secret word: ' + ('_ ' * len(secret_word)))

MAX_TRIES = 6
error_counter = 0
game_over = False
old_letters_guessed = []

# The main loop game

while not game_over:

    # The letter guessed by the user 

    letter_guessed = input('Guess a Letter: ').lower()

    # Checking certain conditions of the letter guessed 

    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        print('Invalid input')
        
    elif letter_guessed in old_letters_guessed:
        print("You alreay guessed this letter, try another. ")
    else:
        old_letters_guessed.append(letter_guessed)
        
    if letter_guessed not in secret_word:
        print("You wrong!")
        error_counter += 1
        print(ASCII_ART.ASCII_ART[error_counter])
    
    # Checking if the letter is in the secret word
    # Print the guesses on the screen
    
    word_guess = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_guess.append(letter)
        else:
            word_guess.append('_ ')
    word_complete = ''.join(word_guess)
    print(word_complete)

    # Checking if the user pass the MAX TRIES, he loose the game and loop break
        
    if error_counter == MAX_TRIES:
        game_over = True
        print(f"Game Over! the secret word was {secret_word}")
    
    # Checking if the user complete the word guess and won the game
    
    if len(word_complete) == len(secret_word):
        print(f"You won the game! the secret word is {secret_word}")
        break