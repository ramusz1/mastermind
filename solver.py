
import argparse
import itertools
import random
from collections import Counter
from copy import deepcopy


class Solver:

    def __init__(self):
        # initialize solutions
        self.solutions = list(itertools.product([1,2,3,4,5,6], repeat=4))
        # self.solutions = list(itertools.combinations_with_replacement([1,2,3], 3))

    def guess(self):
        return random.choice(self.solutions)

    def addFeedback(self, guess, feedback : str):
        new_solutions = []
        black_n = feedback.count("b")
        white_n = feedback.count("w")
        matching_colors = black_n + white_n
        for s in self.solutions:
            if self._matchingPositions(s, guess) == black_n and self._matchingColors(s, guess) == matching_colors:
                new_solutions.append(s)

        self.solutions = new_solutions
        print(len(self.solutions))

    @staticmethod
    def _matchingPositions(solution, guess):
        k = 0
        for s,g in zip(solution, guess):
            if s == g:
                k += 1
        return k

    @staticmethod
    def _matchingColors(solution, guess):
        guess_colors_set = Counter(guess)
        k = 0
        for s in solution:
            if s in guess_colors_set and guess_colors_set[s] > 0:
                k += 1
                guess_colors_set[s] -= 1

        return k


if __name__ == "__main__":
    print(
"""
Mastermind game solver
for each guess provide a feedback string:
    for each matching positions write a b
    for each matching color (for letters not matching exactly) write a w
example:
    solution: 1,2,3
    guess: 1,3,2
    feedback: bw
"""
    )

    s = Solver()
    done = False
    while not done:
        guess = s.guess()
        print("My guess", guess)
        feedback = input("provide feedback: ").lower()
        if feedback.count("b") == len(guess):
            done = True
           
        s.addFeedback(guess, feedback)

    print(f"Done! Solution : {guess}")

