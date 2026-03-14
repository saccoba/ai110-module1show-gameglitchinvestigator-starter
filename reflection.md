# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- Ans: The game is giving the opposite hint. When a number small than the secret is guessed, it tells the player to go lower instead of higher, which misleads the player.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  Ans: 1. The hint logic is reversed (tells the player the wrong direction)
  2. The displayed number range does not match the selected difficult level

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Ans: I used copilot and Chatgpt
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Ans: On line 34, we changed st.session_state.attempts = 1 to st.session_state.attempts = 0
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- Copilot was suggesting a change of every code inside app.py to some random codes, i tried it at first, but everything was scratching.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Ans: I have to test and see if i will get the desired answer.
- Describe at least one test you ran (manual or using pytest)
- Ans: After fixing some bugs, i tried to run the test_logic.py to make sure everything was ok.
- and what it showed you about your code.
- Ans: the code was unable to find the located path, so was getting error.
- Did AI help you design or understand any tests? How?
- Ans: AI help explained to me how to locate the file in the folder.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
