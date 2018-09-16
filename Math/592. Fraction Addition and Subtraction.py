"""
Given a string representing an expression of fraction addition and subtraction, 
you need to return the calculation result in string format. 
The final result should be irreducible fraction. 
If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1.
So in this case, 2 should be converted to 2/1.

Example 1:

Input:"-1/2+1/2"
Output: "0/1"

"""

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        def add(a, b):
            if a == "0/1":
                return b

            def gcd(a, b):
                while b != 0:
                    a, b = b, a % b
                return a

            (an, ad), (bn, bd) = map(int, a.split("/")), map(int, b.split("/"))
            #print ("an=%d"%an, "ad=%d"%ad)
            lcm = (ad * bd) / (gcd(ad, bd))
            an, bn = an * (lcm / ad), bn * (lcm / bd)
            n = an + bn
            g = gcd(n, lcm)
            return str(n / g) + "/" + str(lcm / g)

        print "at first expression=%s"%expression
        expression += "+"
        print "after += expresssion=%s"%expression
        ans = "0/1"
        start = 0
        for i in range(1,len(expression)):
            print "expression[%d]="%i,"%s"%expression[i]
            if expression[i] in ["+", "-"]:
                num = expression[start:i]
                print "num=%s"%num
                ans = add(ans, num)
                start = i
        return ans if ans[0] != "+" else ans[1:]


if __name__=="__main__":
    print (Solution().fractionAddition("-1/2+1/2"))
