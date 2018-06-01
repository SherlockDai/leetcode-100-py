# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0 and l1.next is None:
            return l2
        if l2.val == 0 and l2.next is None:
            return l1
        carry = 0
        dummy = ListNode(0)
        currentNode = dummy
        while l1 and l2:
            sum = carry + l1.val + l2.val
            carry = sum // 10
            val = sum % 10
            newNode = ListNode(val)
            currentNode.next = newNode
            currentNode = newNode
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = carry + l1.val
            carry = sum // 10
            val = sum % 10
            newNode = ListNode(val)
            currentNode.next = newNode
            currentNode = newNode
            l1 = l1.next
        while l2:
            sum = carry + l2.val
            carry = sum // 10
            val = sum % 10
            newNode = ListNode(val)
            currentNode.next = newNode
            currentNode = newNode
            l2 = l2.next
        if carry == 1:
            newNode = ListNode(1)
            currentNode.next = newNode
        return dummy.next

