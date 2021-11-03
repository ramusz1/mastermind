from solver import Solver
import unittest
from collections import Counter

class TestSolver(unittest.TestCase):

    def test_matchingPositions(self):

        def testSingleCase(k, solution, guess):
            self.assertEqual(Solver._matchingPositions(guess, solution), k)

        testSingleCase(3, [1,2,3,4], [1,3,3,4])
        testSingleCase(2, [5,6,3,4], [1,3,3,4])
        testSingleCase(0, [1,2,3,4], [5,6,6,5])
        testSingleCase(1, [1,1,2,3], [1,4,4,4])
        testSingleCase(2, [4,1,6,3], [4,1,4,4])
        testSingleCase(4, [1,6,2,3], [1,6,2,3])
        testSingleCase(4, [6,6,6,6], [6,6,6,6])
        testSingleCase(1, [1,2,3,1], [2,3,3,5])

    def test_matchingColors(self):

        def testSingleCase(k, solution, guess):
            self.assertEqual(Solver._matchingColors(solution, guess), k)

        testSingleCase(4, [1,2,3,4], [1,3,4,2])
        testSingleCase(2, [5,6,3,4], [1,6,2,4])
        testSingleCase(0, [1,2,3,4], [5,6,6,5])
        testSingleCase(1, [1,1,2,3], [1,4,4,4])
        testSingleCase(2, [2,1,2,6], [6,4,2,4])
        testSingleCase(4, [5,6,6,6], [6,6,5,6])
        testSingleCase(0, [1,1,2,3], [6,5,4,4])
        testSingleCase(2, [1,2,3,1], [2,3,3,5])



if __name__ == "__main__":
    unittest.main()

