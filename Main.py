import random

welcome_banner = """
                Welcome to Guess The Word!

    In this game you will have to guess a word. Good luck! 
"""

playing = True
rounds = 0

print(welcome_banner)

def guess_the_word(rounds):
    words_list = ["apple", "banana", "orange", "grape", "watermelon"]
    random_word = random.choice(words_list)

    while playing:
        guess = input("Guess a word: ")
        
        if guess.lower() == random_word:
            print(f"Congratulations! That's correct. You guessed it in {rounds} rounds.")
            return True
        else:
            print("Not quite.")

            if rounds == 3:
                print(f"Hint: The word has {len(random_word)} letters.")
            elif rounds == 5:
                print(f"Hint: The word starts with the letter '{random_word[0]}'.")
            
            rounds += 1

    return False

while not guess_the_word(rounds):
    pass
