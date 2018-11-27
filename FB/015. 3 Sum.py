"""
1，先将数组排序。
2，排序后，可以按照TwoSum的思路来解题。怎么解呢？
可以将num[i]的相反数即-num[i]作为target，然后从i+1到len(num)-1的数组元素中寻找两个数使它们的和为-num[i]就可以了。下标i的范围是从0到len(num)-3。
3，这个过程要注意去重。
4，时间复杂度为O(N^2)。
map() function returns a list of the results
after applying the given function to each item of a given iterable (list, tuple etc.)
"""
class Solution(object):

    def twoSum(self, nums, target):
        idxDict = dict()

        idx_list = []
        for idx, num in enumerate(nums):
            if target - num in idxDict:
                 idx_list.append([idxDict[target - num], idx])
            idxDict[num] = idx
        return idx_list



    def threeSum(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num.sort()
        res = dict()
        result = []
        for i in range(len(num) - 2):
            if (i == 0 or num[i] > num[i-1]) and num[i] <= 0:
                left = i + 1
               # print('left=%d'%left)
                result_idx = self.twoSum(num[left:], -num[i])
                for each_idx in result_idx:
                    each_result = [num[i], num[each_idx[0]+left], num[each_idx[1]+left]]
                   # print ('each_result=',each_result)
                    #print ('result=',result)
                   # print ('res=', res)
                    if str(each_result) not in res:
                        res[str(each_result)] = each_result
        for value in res.values():
            result.append(value)
        return result



if __name__=="__main__":
    print (Solution().threeSum([-1,0,1,2,-1,-4]))
