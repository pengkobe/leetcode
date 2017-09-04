# -*- coding: utf-8 -*-
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head;
    B_TNode = head;
    TNode = head.next;
    while TNode:
        if B_TNode.val == TNode.val:
            B_TNode.next = TNode.next;
            if TNode.next:
               TNode = TNode.next;
            else:
                break;
        else:
            B_TNode = TNode;
            if TNode.next:
                TNode = TNode.next;
            else:
                break;
    return head;