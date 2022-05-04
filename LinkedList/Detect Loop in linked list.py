# Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.
#
# Example 1:
#
# Input:
# N = 3
# value[] = {1,3,4}
# x(position at which tail is connected) = 2
# Output: True
# Explanation: In above test case N = 3.
# The linked list with nodes N = 3 is
# given. Then value of x=2 is given which
# means last node is connected with xth
# node of linked list. Therefore, there
# exists a loop.

def hasCycle(head) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Logic :-
#
# Imagine the following example: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3, the list with loop. Idea is to use two
# pointers, one is slow and one is fast, let us do several steps:
#
# At the beginning, both of them at number 1. Next step, slow pointer at 2 and fast at 3. Next step, slow pointer at
# 3 and fast at 5. Next step, slow pointer at 4 and fast at 3. Next step, slow pointer at 5 and fast is also 5,
# so we have the same element, and we return True. If we do not have loop we will never have equal elements,
# if we have loop, because slow pointer moves with speed 1 and fast with speed 2, fast pointer will always gain slow
# one.
#
# Complexity: time complexity is O(n), space complexity is O(1).
