import random
print("Guess the name of the marvel character with the help of their dialogues")
words = {"tonystark": "I am Iron Man", "captainamerica": "I can do this all day",
         "thor": "bring me thanos", "hulk": "smash", "blackpanther": "Wakanda Forever", 
         "peterparker":"Real name of spider man"}
random_word = random.choice(list(words.keys()))
print(words[random_word])
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in random_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\nCongratulations you won")
        print(f"The Character is {random_word}")
        break
    guess = input("\nGuess the word\n")
    guesses += guess
    if guess not in random_word:
        turns -= 1
        print("Wrong!")
        print(f"You have {turns} turns left")
    if turns == 0:
        print("Better Luck Next Time")