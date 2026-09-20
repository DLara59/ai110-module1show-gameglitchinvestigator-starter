# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is have the user guess a randomly generated number correctly within 8 attempts, with hints being optional.
The user is allowed to reference these hints as they try to achieve the highest possible score.
The users' skills in guess are tested by the game and the game is designed to have the user guessing numbers, while helping them guess correctly.

- [ ] Detail which bugs you found.
The bugs that I found involved the secret number and hints not matching the guesses correctly. 
For example, if I guess 13, the game would hint "Go LOWER", however the secret number was 18.
There were multiple logical inconsistencies within the code. 
Another example was the inability to start a new game after the game had concluded; the "New Game" button was broken.

- [ ] Explain what fixes you applied.
The fixes that I applied were overall program improvement fixes, such as fixing the aforementioned bugs in the Hints and Secret Numbers not being accurate.
I also worked with the AI to fix the ""New Game" button in order to allow the user to quickly begin a new game, as it was intended to work.
Another fix that I worked on was the error in point calculation and accumulation that had occurred when the AI fixed the earlier issues. 
Once the error was found and the logic had been repaired, we adjusted the point calculation to increase and decrease by values that increment and decrement to a total of 100 with each guess being used.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- User has eight attempts to guess a random number in the range of 1 - 100 -->
2. <!-- User enters a guess of 53; their first of 8 total attempts-->
3. <!-- Game returns a hint that says "Go LOWER!"-->
4. <!-- User enters a guess of 85-->
5. <!-- Game returns a hint that says "Go HIGHER!" -->
6. <!-- User enters a guess of 77 -->
7. <!-- Game returns "Correct! You won"; shows user the solution and their final score based on points awarded-->
8. <!-- User selects "New Game" and their score compounds or decreases based on their next game performance -->
9. <!-- Score is dependent on number of guesses needed to solve the game; adding up to 100 points per game or subtracting up to 100 points per game -->


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

![<# alt text #>](../Desktop/Screenshot%202026-09-20%20at%203.03.38%E2%80%AFAM.heic "Screenshot")
Screenshot 2026-09-20 at 3.03.38 AM.heic

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================

platform darwin -- Python 3.13.2, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/dave/ai110-module1show-gameglitchinvestigator-starter-main
configfile: pytest.ini
plugins: anyio-4.15.1
collected 7 items                                                 

tests/test_game_logic.py .......                            [100%]

======================== 7 passed in 0.01s ========================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
