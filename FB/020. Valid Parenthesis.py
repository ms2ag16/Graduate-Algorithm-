class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ('(', '{', '[')
        right = (')', '}', ']')

        stack = []

        for ele in s:
            if ele in left:
                stack.append(ele)
            if ele in right:
                if not len(stack):
                    return False
                curr_left = stack.pop()
                if left.index(curr_left) != right.index(ele):
                    return False
        return len(stack) == 0

if __name__=="__main__":
    print Solution().isValid('(]')
