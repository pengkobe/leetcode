# -*- coding: utf-8 -*-
# Given two binary trees, write a function to check if they are equal or not.
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True;
    elif not p:
        return False;
    elif not q:
        return False;

    if p.val == None and q.val == None:
        return True;
    elif p.val == None:
        return False;
    elif q.val == None:
        return False;
    if p.val == q.val:
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else:
        return False;