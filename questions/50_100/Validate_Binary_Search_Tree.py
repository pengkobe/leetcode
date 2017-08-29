# -*- coding: utf-8 -*-
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 也许翻过来思考会更好
def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def sub_isValidBST(node, pre, type):
        if not node:
            return True;
        if (node.left.val and node.left.val > node.val):
            return False;
        if (node.right.val and node.right.val < node.val):
            return False;
        if not node.left.val and not node.right.val:
            return True;
        else:
            if not pre:
                return sub_isValidBST(node.left, node.val, 'left') and sub_isValidBST(node.right, node.val, 'rigth');
            else:
                if (type == 'left' and node.right.val and node.right.val > pre) or (type == 'rigth' and node.left.val and node.left.val < pre):
                    return False;
                else:
                    return sub_isValidBST(node.left, node.val, 'left') and sub_isValidBST(node.right, node.val, 'rigth');

    # 程序开始
    pre = None;
    return sub_isValidBST(root, pre, 'left');


# 非常成功的失败案例,只考虑到了 2 级
# [3,1,5,0,2,4,6,null,null,null,3]
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sub_isValidBST(node, pre, type):
            if not node:
                return True;
            if not node.left and not node.right:
                return True;
            if (not node.left or node.left.val < node.val) and (not node.right or node.right.val > node.val):
                if not pre:
                    return sub_isValidBST(node.left, node.val, 'left') and sub_isValidBST(node.right, node.val, 'right');
                else:
                    print(pre, type)
                    if (type == 'left' and (not node.right or node.right.val < pre)):
                        return sub_isValidBST(node.left, node.val, 'left') and sub_isValidBST(node.right, node.val, 'right');
                    if (type == 'right' and (not node.left or node.left.val > pre)):
                        return sub_isValidBST(node.left, node.val, 'left') and sub_isValidBST(node.right, node.val, 'right');
            print('h3')
            return False;

        # 程序开始
        pre = None;
        return sub_isValidBST(root, pre, 'left');




## 只打败了 3.8%，哭晕在厕所
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sub_isValidBST(node, maxV, minV):
            if not node:
                return True;
            if not node.left and not node.right:
                return True;
            if (not node.left or node.left.val < node.val) and (not node.right or node.right.val > node.val):
                if maxV and node.right:
                    if node.right.val >= maxV:
                        print('xx')
                        return False;
                if minV and node.left:
                    if node.left.val <= minV:
                        print('xx')
                        return False;
                if maxV and node.val > maxV:
                    maxV = node.val;
                if minV and node.val < minV:
                    minV = node.val;
                print(node.val,maxV,minV)
                return sub_isValidBST(node.left,node.val,minV) and sub_isValidBST(node.right,maxV,node.val);
            else:
                return False;

        return sub_isValidBST(root,None,None);


## 参考答案: 中序遍历