"""
 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1

"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxVal=max(nums)
        maxIdx=nums.index(maxVal)
        root=TreeNode(maxVal)
        root.left=self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right=self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return root

if __name__=="__main__":
    print (Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]).val)