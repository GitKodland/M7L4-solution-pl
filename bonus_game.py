from speech import speech
from random import choice, randint
import time

# Difficulty levels
levels = {
    "easy": ["agenda", "ami", "souris"],
    "medium": ["ordinateur", "algorithme", "développeur"],
    "hard": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def play_game(level):
    words = levels.get(level, [])  # Wybieranie słów na podstawie poziomu trudności
    if not words:
        print("Incorrect difficulty level.")
        return

    score = 0
    num_attempts = 3  # Liczba prób na słowo

    for _ in range(len(words)):
        random_word = choice(words)
        print(f"Please pronounce the word {random_word}")
        recog_word = speech()
        print(recog_word)
        
        if random_word == recog_word:
            print("That's right!")
            score += 1
        else:
            print(f"Something is wrong. The word is: {random_word}")

        time.sleep(2)  # Przerwa między słowami
        
    print(f"Game over! Your score is: {score}/{len(words)}")

# Wybierz poziom trudności
selected_level = input("Select the difficulty level (easy/medium/hard): ").lower()
play_game(selected_level)