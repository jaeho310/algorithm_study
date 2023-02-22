class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        length = len(temp)
        for i in range(length//2):
            if temp[i] != temp[-i-1]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(-10))