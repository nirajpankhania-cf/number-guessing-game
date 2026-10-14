# number-guessing-game

| | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---------------|------------|-----------------|---------------|-------|
| 1 | set easy difficulty | input 1 at difficulty selection | prints 'easy' | prints 'easy' | Yes |
| 2 | set medium difficulty | input 2 at difficulty selection | prints 'medium' | prints 'medium' | Yes |
| 3 | set hard difficulty | input 3 at difficulty selection | prints 'hard' | prints 'hard' | Yes |
| 4 | low guess | guessed lower than secret_number | prints 'too low' | prints 'too low' | Yes |
| 5 | high guess | guessed higher than secret_number | prints 'too high' | prints 'too high' | Yes |
| 6 | correct guess (classic) | guessed lower than secret_number | prints 'correct' and total attempts | prints 'correct' and total attempts  | Yes |
| 7 | correct guess (time challenge) | guessed lower than secret_number | prints 'correct!', attempts remaining and time remaining | prints 'correct' and total attempts  | Yes |
| 8 | non numerical guess | put in a letter as a guess | prints 'invalid guess, no attempts consumed', attempts remain the same | prints 'invalid guess, no attempts consumed', attempts remain the same | Yes |
| 9 | out of range guess | put in 501 as a guess | prints 'out of range, no attempts consumed', attempts remain the same | prints 'out of range, no attempts consumed', attempts remain the same | Yes |
| 10 | blank guess | enter '' as a guess | prints 'invalid guess, no attempts consumed', attempts remain the same | prints 'invalid guess, no attempts consumed', attempts remain the same | Yes |
| 11 | (time challenge) easy difficulty attempts, upper and range | input 1 at difficulty selection | prints '10', '50', '1-50' | prints '10', '50', '1-50' | Yes |
| 12 | (time challenge) medium difficulty attempts, upper and range | input 2 at difficulty selection | prints '8', '100', '1-100' | prints '8', '100', '1-100' | Yes |
| 13 | (time challenge) hard difficulty attempts, upper and range | input 3 at difficulty selection | prints '10', '500', '1-500' | prints '10', '500', '1-500' | Yes |
| 14 | (classic) attempts | choose classic mode | prints '0' | prints '0' | Yes |
| 15 | out of guesses | time challenge, guess wrong | prints 'out of guesses' and secret number | prints 'out of guesses' and secret number | Yes |
| 16 | out of guesses | time challenge, guess wrong | prints 'time's up! Game over' and secret number | prints 'time's up! Game over' and secret number | Yes |
| 17 | timer works | make guesses | prints 'remaining time' decrementing correctly | prints 'remaining time' decrementing correctly | Yes |
