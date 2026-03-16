# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran it, the game allowed a user to enter a number into the guess bar. Once you entered something in, 
it would give you a hint as to where the secret number was in relation to your guess. There were other features
available like changing appearance and changing the difficulty level. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
I noticed that the hints were wrong and they were saying the opposite thing than what it was meant to be. 
Also difficulty for normal was seemingly harder than the difficulty set for hard. The secret number is also
changed on every even attempt and wrong guesses give you bonus points when it shouldn't. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example of an AI suggestion that was correct was changing the hint logic. It did the low hint when the
number was lower than the secret and the high hint when the opposite occured. I verified this by running the game
using the streamlit command and it displayed the right hints. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
There was no AI suggestion that was incorrect or misleading. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I made some tests using pytest and ran those first. If those were passing, I would move on to making sure
the actual game was working or not. If those were failing, I would reiterate with AI. Once the actual game
was working, that is when I knew whether or not the actual bug was fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The check guess test correctly compares numbers when the secret is an integer. It calls check_guess with some
  guess and secret number and then displays some hint about the guess in relation to the secret number.
  This showed whether the hint was right or not. 
- Did AI help you design or understand any tests? How?
Yes, it helped me design some of the tests in the sense that it gave me the ideas behind some of the tests. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you click a button or type something in Streamlit, the entire script reruns from scratch, like refreshing a page. Regular variables reset on every rerun, so Streamlit gives you st.session_state, a special dictionary that persists across reruns. That's how the game remembers your score and attempts between guesses.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Being able to properly test my code by partnering with an AI to make the tests is something I want
  to reuse in the future labs and projects.
- What is one thing you would do differently next time you work with AI on a coding task?
I would make sure I try to make the AI fumble a little bit since I think fixing the bugs I chose for this
project were too easy to fix for AI.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It has made me think much better about AI generated code in the sense that now I know it isn't always 
perfect and that reassures me. Additionally, it lets me know that people would still have to check AI code
here and there once it inevitably fully takes over the jobs.