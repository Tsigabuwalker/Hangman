import random

def choose_word(difficulty):
    word_lists = {
        'easy': ["cat", "dog", "fish", "bird"],
        'medium': ["python", "hangman", "challenge", "programming"],
        'hard': ["developer", "executable", "algorithm", "functionality"]
    }
    return random.choice(word_lists[difficulty])

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |  
           -
        """,
        """
           -----
           |   |
           |   O
           |  
           |  
           -
        """,
        """
           -----
           |   |
           |  
           |  
           |  
           -
        """,
    ]
    return stages[tries]

def play_hangman():
    score = 0
    while True:
        print("Choose a difficulty level: easy, medium, hard")
        difficulty = input().lower()
        
        if difficulty not in ['easy', 'medium', 'hard']:
            print("Invalid difficulty. Please choose again.")
            continue
            
        word = choose_word(difficulty)
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        
        print("Let's play Hangman!")
        print(display_hangman(tries))
        print(word_completion)

        while not guessed and tries > 0:
            guess = input("Please guess a letter or word (or type 'hint' for a hint): ").lower()
            
            if guess == 'hint':
                if any(letter not in guessed_letters for letter in word):
                    hint_letter = next(letter for letter in word if letter not in guessed_letters)
                    print(f"Hint: One of the letters is '{hint_letter}'.")
                else:
                    print("No hints available; you've guessed all the letters!")
                continue
            
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You've already guessed that letter.")
                elif guess not in word:
                    print("That letter is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Good job! That letter is in the word.")
                    guessed_letters.append(guess)
                    word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You've already guessed that word.")
                elif guess != word:
                    print("That word is not correct.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Invalid input. Please guess a letter or a word.")

            print(display_hangman(tries))
            print(word_completion)

        if guessed:
            print("Congratulations! You've guessed the word!")
            score += 1
        else:
            print(f"Sorry, you've run out of tries. The word was '{word}'.")

        print(f"Your current score is: {score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_hangman()