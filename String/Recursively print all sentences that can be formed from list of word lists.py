# Difficulty - Medium
from typing import *


arr = [ ["you", "we",""],
        ["have", "are",""],
        ["sleep", "eat", "drink"]]

R = 3
C = 3

class Solution:
    def printSentencesUtil(self, arr: List[str], m: int, n: int, output: List[str]):

        # Add current word to output array
        output[m] = arr[m][n]

        # If this is last word of current output sentence, then
        # Print the output sentence.
        if m == R-1:
            for i in range(R):
                print(output[i], end=" ")
            print()
            return

        # Recur for the next row
        for i in range(C):
            if arr[m+1][i] != "":
                self.printSentencesUtil(arr, m+1, i, output)

    def printSentences(self, arr: List[str]):

        # Create an array to store the Sentence
        output = R * [""]

        # Consider all words for first row as starting Points
        # and print all sentences
        for i in range(C):
            if arr[0][i] != "":
                self.printSentencesUtil(arr, 0, i, output)

x = Solution()
x.printSentences(arr)
