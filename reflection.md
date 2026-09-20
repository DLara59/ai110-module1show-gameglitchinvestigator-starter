# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
When I started the game, I immediately noticed the logic of the game was broken. I could make this conclusion after trying my first test of the game and not receiving desired results, such as appropriate hints, appropriate scores, and an option to restart a test without having to rerun the code. The "New Game" option did not restart the game, nor did re-running the program from the webpage; the only thing that allowed a restart was either refreshing the web page or re-running manually through stream lit.

- What did the game look like the first time you ran it?
The game looked pretty sound upon first glance, however, it was only after my first run of the game did I notice the issues. The UI was friendly and the game seemed straight-forward, but i ran into logic-based misconceptions/errors. It was as if the game did not know how to properly behave like a game.

- List at least two concrete bugs you noticed at the start (for example: "the hints were backwards").

The first bug I ran into was the incorrect hints when it came to guessing the solution of the game; I was told to guess higher when the solution ended up being lower than the guesses that I was making.
The second bug that I ran into was the restart feature of the game once the game was complete not correctly restarting the game; instead, the page would appear to frozen.
The third bug that I ran into was the hint asking you to go lower than one, despite the secret number being higher than 0; this resulted in an illogical ask from the system, since the parameters of the program are numbers between 1 and 100, and 0 is not in that range.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| guess of 60 | Too low hint| Go HIGHER! hint shown | none |
| press New Game | Start a new game | New game does not start | none |
| guess of 0 | Go higher | Go LOWER! | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
The AI tool that I used for this project was Co-Pilot, which works within my IDE. I used Copilot, mostly in agent mode, to answer and explain errors within the code. Once I felt as if I was on the same page as the AI, i kept the changed being made or rejected them and reworded my prompt.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I gave the AI a prompt that included testing the output of the game being prematurely displayed to the user before the end of the game and the AI returned the reason being the structure of the flow of logic. This is was indeed correct, as the output was being thrown prior to the end of the game. Therefore, when both the AI and I were on the same page, the AI was able to recommend a fix that I agreed with because it allowed restructuring the logic to flow in a way that made much more sense than it had before.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
One of the suggestions that the AI suggested, which I rejected, was the want to have the score calculations remain at values added or subtracted 100 based on whether the guess was correct or not. For example, if the player could guess the number within 1-8 tries, as long as they guess correctly, they would get 100 score, and the same could be said for a wrong guess, but instead of adding 100, the score would subtract 100. This scoring calculation had been added during one of my earllier code revisions, by pure happenstance, however once I noticed it, I rebutted immediately. My logic was that score should increment and decrement up 100 or down to 100 based on how many attempts a solution takes to reach or not reach, so I had the AI do that instead.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed by running the program myself. Despite the AI testing it on its own, including the pytests, I wanted to see the changed firsthand. I did not trust the words of the AI alone, and did 3 test runs after each bug fix to ensure that the bug was really fixed and nothing had been broken without other aspects of the program.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
One specific test that I ran was after the AI had fixed the hints not being accurate to the solution number. Once I noticed that the bug had been fixed, I dug deeper and tested some more. I noticed that the new game button was still not working, so I instructed that the AI correct this, despite their having overlooked it before.
  
- Did AI help you design or understand any tests? How?
Yes, AI did help me both design and understand the tests being run. This was achieved by how detailed the explanations were. I found myself unafraid to ask more questions and for more explanations, and I found myself doubting the AI more and more, but in a positive way; I found myself understanding how its testing was occurring and trusting my own testing over solely trusting its own.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
