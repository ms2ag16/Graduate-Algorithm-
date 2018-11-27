""" Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res =[]
        self.dfs(s,0 ,res ,'')
        return res

    def dfs(self, s, seg, ips, ip):
        if seg==4:
            if s=='':
                ips.append(ip[1:])
            return
        for i in range(1,4):
            if i<=len(s):
                if int(s[:i])<=255:
                   # print ('current s=%s'%s[i:])
                    self.dfs(s[i:], seg+1, ips, ip+'.'+s[:i])
                   # print ('current ips=%s'%ips)
                if s[0]=='0':
                    break

if __name__=="__main__":
    print (Solution().restoreIpAddresses('25525511135'))



