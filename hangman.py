import random 

def chosen():
    words = [
    "elephant", "guitar", "ocean", "mountain", "bicycle",
    "bookshelf", "garden", "candle", "painting", "camera",
    "giraffe", "sunflower", "island", "rainbow", "coffee",
    "umbrella", "butterfly", "moonlight", "sandcastle", "treasure",
    "pineapple", "jazz", "skyscraper", "firefly", "waterfall",
    "whale", "carousel", "paradise", "mirage", "adventure",
    "cactus", "whisper", "cinnamon", "lighthouse", "serenade",
    "harmony", "cosmos", "silhouette", "bliss", "radiant",
    "carousel", "voyage", "cottage", "mystique", "tranquil",
    "cascade", "twilight", "fountain", "serenity", "harbor"]

    return random.choice(words)

def show_word(word1, guessed_letters):
    display1 = ""
    for letter in word1:
        if letter in guessed_letters:
            display1+=letter
        else:
            display1+= "_"
    return display1

def hangman_show(attempts):
    hangman_images = [
        """
         ------
         |    |
         |
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\ 
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\ 
         |   /
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\ 
         |   / \ 
         |
        ---
        """
    ]

    print(hangman_images[6 - attempts])


def hangman():
    chosen_word = chosen()
    guessed_letters = []
    attempts = 7

    print("WELCOME TO THE HANGMAN GAME")
    print(show_word(chosen_word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("LETTER GIVEN NOT VALID")
            continue

        if guess in guessed_letters:
            print("LETTER HAS ALREADY BEEN GUESSED")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            attempts -= 1
            print("---INCORRECT --- Attempts left:" + str(attempts))
            hangman_show(attempts)
        else:
            print("----CORRECT GUESS----")

        display2 = show_word(chosen_word, guessed_letters)
        print(display2)

        if "_" not in display2:
            print("THE WORD HAS BEEN GUESSED")
            break

    if "_" in display2:
        print("YOU HAVE RUN OUT OF ATTEMPTS----The word was:" + str(chosen_word))
        print("""
              !!!! YOU DIED !!!!! """)


hangman() 
