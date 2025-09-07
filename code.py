import random

def hangman():
    # Predefined list of words
    words = ["apple", "banana", "orange", "grapes", "mango"]
    word = random.choice(words)  # Randomly choose a word
    guessed_letters = []         # Store guessed letters
    attempts = 6                 # Number of chances

    print("🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    # Create hidden version of the word
    display = ["_"] * len(word)

    while attempts > 0 and "_" in display:
        print("\nWord: ", " ".join(display))
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is in the word
        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("❌ Wrong guess!")
            attempts -= 1

    # Final result
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n😢 Game Over! The word was:", word)


# Run the game
hangman()
