# -*- coding: utf-8 -*-
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.

## 只击败了 16.1% 的用户
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2;
    if not l2:
        return l1;

    if l1.val <= l2.val:
        ret = l1;
        l1 = l1.next;
    else:
        ret = l2;
        l2 = l2.next;
    temp = ret;
    while l1 and l2:
        if l1.val <= l2.val:
            temp.next = l1;
            temp = l1;
            l1 = l1.next
        else:
            temp.next = l2;
            temp = l2;
            l2 = l2.next
    if l1:
        temp.next = l1;
    if l2:
        temp.next = l2;    
    return ret;
