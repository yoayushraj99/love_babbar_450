# Difficulty - Medium
from typing import *


class Solution:
    def runCustomerSimulation(self, n, seq):
        # seen[i] = 0, indicates that customer 'i' is not in cafe
        # seen[1] = 1, indicates that customer 'i' is in cafe but
        #             computer is not assigned yet.
        # seen[2] = 2, indicates that customer 'i' is in cafe and
        #             has occupied a computer.
        max_char = 26
        seen = [0] * max_char

        res = 0
        occupied = 0    # to keep track of occupied

        for i in range(len(seq)):
            # Find index of current character in seen[0...25]
            ind = ord(seq[i]) - ord('A')

            # If first occurence of 'seq[i]'
            if seen[ind] == 0:
                # set the current character as seen
                seen[ind] = 1

                # if number of occupied computers is less than n
                # then assign a computer to new customer
                if occupied < n:
                    occupied += 1

                    # Set the current character as occupying a computer
                    seen[ind] = 2

                # ELse this customer cannot get a computer, increment
                else:
                    res += 1

            # if this is second occurrence of 'seq[i]'
            else:
                # Decrement occupied only if this customer
                # was using a computer
                if seen[ind] == 2:
                    occupied -= 1
                seen[ind] = 0

        return res


x = Solution()
print (x.runCustomerSimulation(2, "ABBAJJKZKZ"))
print (x.runCustomerSimulation(3, "GACCBDDBAGEE"))
print (x.runCustomerSimulation(3, "GACCBGDDBAEE"))
print (x.runCustomerSimulation(1, "ABCBCA"))
print (x.runCustomerSimulation(1, "ABCBCADEED"))

# Time complexity of above solution is O(n) and
# extra space required is O(CHAR_MAX) where CHAR_MAX is total number of possible characters in given sequence.
