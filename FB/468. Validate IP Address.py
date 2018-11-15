class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.isIPv4(IP):
            return 'IPv4'
        if self.isIPv6(IP):
            return 'IPv6'
        return 'Neither'
        
    def isIPv4(self,IP):
        parts=IP.split('.')
        if len(parts)!=4:
            return False
        for part in parts:
            if not part.isdigit(): return False
            if not part: return False
            if part[0]=='0' and len(part)>1: return False
            if int(part)>255 or int(part)<0: return False
        return True
            
            
    
    def isIPv6(self,IP):
        parts=IP.split(':')
        if len(parts)!=8:
            return False
        for part in parts:
            if not part: return False
            if len(part)>4:
                return False
            if any(i not in string.hexdigits for i in part):
                return False
        return True
