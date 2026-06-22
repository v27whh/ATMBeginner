# 🏦 ATMBeginner
A script I put together to practice the core basics of Python by building something practical: a functional, secure ATM simulator.

Instead of just printing static text, I wanted to build something interactive that handles real logic, tracks user data, and won't completely explode if someone accidentally inputs a typo.

# ⚙️ How it was made:
1. The Loop (while True): Keeps the program running continuously so you can do multiple transactions in one session, rather than kicking you out after one action.

2. Menu Routing (if / elif / else): Directs the user to the right code block based on whether they want to deposit, withdraw, check balance, or exit.

3. PIN Authentication: A simple security step at the start that gives the user 3 attempts to get in before locking them out.

4. Persistent Balance: Keeps track of your cash mathematically so your balance updates properly across multiple inputs.

5. Error Prevention (try / except): My favorite part. If the program asks for a number and you type letters like "abc", this catches the mistake, handles it nicely, and keeps the program running smoothly instead of throwing a massive red error screen.

6. f-strings: Used to easily inject variable data (like the live balance) straight into text outputs.

# 👤 Author
Created by: [ Youssef Hassan Abdalla ]

Project Name: ATMBeginner Project

Find me on: [ https://github.com/v27whh ]

"Built to make learning Python simple, secure, and interactive."
