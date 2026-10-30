class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome =  "".join(c.lower() for c in s if c.isalnum())
        reversed_palindrome = palindrome[::-1]

        for i in range(len(palindrome)):
            if palindrome[i] != reversed_palindrome[i]:
                return False
        return True