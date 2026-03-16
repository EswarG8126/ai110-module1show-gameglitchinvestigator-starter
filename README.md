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
The game's purpose is to entertain by letting the user play a simple guessing game. 
- [ ] Detail which bugs you found.
The bugs I found were mostly large like the normal being set to be harder than the hard mode, the hints
not saying the right things, and the secret number getting corrupted every few guesses.
- [ ] Explain what fixes you applied.
I made sure the hints were saying the right things and also made sure the secret number won't get
changed every few guesses like it was before (making the game much less stressful for the user).

## 📸 Demo

Couldn't seem to put it here so attached it to the repo as an image.

## 🚀 Stretch Features

N/A
