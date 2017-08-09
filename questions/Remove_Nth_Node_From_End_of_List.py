# -*- coding: utf-8 -*-

# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## 错误: remove the nth node from the end of list
# def removeNthNode(head,n):
#     if n == 1:
#         if head.next:
#             head = head.next;
#         else:
#             return None;
#     if not head.next:
#         return None;
#     b_node = head;
#     node = head.next;
#     count = 2;
#     while count <= n:
#         b_node = node
#         if not node.next:
#             return None;
#         else:
#             node = node.next;
#         count +=1;
#     if node.next:
#         b_node.next = node.next;
#     else:
#         b_node.next = None;
#     return head;

# Next challenges: Reverse Nodes in k-GroupConvert Sorted List to Binary Search TreeLongest Word in Dictionary through Deleting


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head;
        count = 1;
        while node.next:
            if not node.next:
                break;
            else:
                node = node.next;
                count +=1;
        n = count - n +1;
        if n == 1:
            if head.next:
                head = head.next;
                return head;
            else:
                return None;
        b_node = head;
        node = head.next;
        count = 2;
        print n; 
        while count < n and node:
            b_node = node
            node = node.next;
            count +=1;
        if node.next:
            b_node.next = node.next;
        else:
            b_node.next = None;
        return head;