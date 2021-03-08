

class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        length = len(str(N))
        sum = 0
        for i in str(N):
            sum +=(int(i) ** length)

        if sum == N:
            print("True")
        else:
           print(sum, "False")



Solution().isArmstrong(153)
Solution().isArmstrong(13543)