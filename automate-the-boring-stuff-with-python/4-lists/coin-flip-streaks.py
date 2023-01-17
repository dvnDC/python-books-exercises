"""
"Coin Flip Streaks
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and
“T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100 random
coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random
(to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails
in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at
being random.
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated
list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of
randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it.
Put all of this code in a loop[…]”

Excerpt From
Automate the Boring Stuff with Python
Al Sweigart
This material may be protected by copyright.
"""

import random


numberOfStreaks = 0
for experimentNumber in range(10000):
    flips = [random.choice(["H", "T"]) for _ in range(100)]
    for i in range(len(flips) - 6):
        if flips[i] == flips[i + 1] == flips[i + 2] == flips[i + 3] == flips[i + 4] == flips[i + 5] == flips[i + 6]:
            numberOfStreaks += 1
            break
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
