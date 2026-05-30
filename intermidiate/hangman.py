@@ -0,0 +1,60 @@
import random
def play_hangman():
    words = ["python", "internship", "developer", "shadowfox", "programming"]
    while True:  # Play again loop
        word = random.choice(words)
        guessed_letters = []
        incorrect_guesses = 0
        max_attempts = 6
        print("\nWelcome to Hangman!")
        # Game loop
        while incorrect_guesses < max_attempts:
            # Display word
            display_word = ""
            for letter in word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "
            print("\nWord:", display_word)
            print("Incorrect guesses left:", max_attempts - incorrect_guesses)
            print("Guessed letters:", guessed_letters)
            # Win condition
            if "_" not in display_word:
                print("Congratulations! You guessed the word:", word)
                break

            # User input
            guess = input("Enter a letter: ").lower()

            # Input validation
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single valid letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            # Check guess
            if guess in word:
                print("Correct guess!")
            else:
                print("Wrong guess!")
                incorrect_guesses += 1

        # Loss condition
        if incorrect_guesses == max_attempts:
            print("You lost! The word was:", word)

        # Play again
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes" and again != "y":
            print("Thanks for playing!")
            break


# Run the game
play_hangman()
