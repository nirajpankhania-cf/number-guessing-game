import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
while True:
    difficulty = input('choose a difficulty mode (easy, medium, hard): ').strip().lower()
    if difficulty in ['easy', 'medium', 'hard']:
        break
    print('try again')

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
while True:
    game_mode = input('choose a game mode (classic, time challenge): ').strip().lower()
    if game_mode in ['classic', 'time challenge']:
        break
    else:
        print('try again')

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
    attempts = 10
else:
    if difficulty == 'easy':
        secret_number = random.randint(1, 50)
        if game_mode == 'classic':
            attempts = 0
        else:
            attempts = 10
    elif difficulty == 'medium':
        secret_number = random.randint(1, 100)
        if game_mode == 'classic':
            attempts = 0
        else:
            attempts = 8
    else:
        secret_number = random.randint(1, 500)
        if game_mode == 'classic':
            attempts = 0
        else:
            attempts = 10

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.
