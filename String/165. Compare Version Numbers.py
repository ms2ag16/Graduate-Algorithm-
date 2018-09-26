"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list=version1.split('.')
        v2_list=version2.split('.')
        for i in range(0, max(len(v1_list), len(v2_list))):
            v1=int(v1_list[i]) if len(v1_list)>i else 0
            v2=int(v2_list[i]) if len(v2_list)>i else 0
            if v1 >v2:
                return 1
            elif v1<v2:
                return -1
        return 0
    
    def recurse(self, version1, version2):
        if version1==version2:
            return 0

        ind1=version1.find('.')
        ind2 = version2.find('.')
        part1 = version1[0:ind1] if ind1 != -1 else version1
        part2 = version1[0:ind2] if ind2 != -1 else version2

        if int(part1)==int(part2):
            remain1=version1[len(part1)+1:] if version1[len(part1)+1:] != '' else '0'
            remain2 = version2[len(part2) + 1:] if version2[len(part2) + 1:] != '' else '0'
            return self.compareVersion(remain1,remain2)
        else:
            return 1 if int(part1)>int(part2) else -1



if __name__=="__main__":
    print Solution().compareVersion(version1 = "1.001", version2 = "1.010")
