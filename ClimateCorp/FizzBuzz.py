class Solution:

    def FizzBuzz(self, num):
        res = []
        res1 = ""
        for i in range(1, num):
            if(i%3 == 0 and i% 5 == 0):
                res.append("FizzBuzz")

            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(i)

        return res


if __name__ == "__main__":
    print Solution().FizzBuzz(11)
