# Difficulty - Easy
from typing import *

class Solution:
	def isPalindrome(self, S):
		for i in range(len(S)//2):
		    if S[i] != S[-1-i]:
		        return 0
		return 1
