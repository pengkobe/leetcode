# -*- coding: utf-8 -*-

# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# [1,1,2]
# [1,2,3]
# [1,1,3,3]
# [3,3,1,1]
# [3,2,2,1]
# [1,2,2,2,3]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 哈哈 击败 90%+ 用户，难得啊
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head;
        TNode = None;
        ret = None;
        start = head;
        end = head.next;
        i = 0;
        while end:
            # 
            if end.val != start.val and i == 0:
                if not TNode:
                    ret = start;
                    TNode = start;
                else:
                    TNode.next = start;
                    TNode = TNode.next;
                start = end;
                end = end.next;
            elif end.val != start.val:
                if TNode:
                    TNode.next = end;
                if not end.next and not TNode:
                    ret = end;
                    break;
                start = end;
                end = end.next;
                i = 0;
            else:
                i +=1;
                end = end.next;
                if not end and TNode:
                    TNode.next = None;
                    break;

        return ret;           