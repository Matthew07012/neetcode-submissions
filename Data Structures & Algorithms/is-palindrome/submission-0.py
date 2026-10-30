class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        is_palindrome = True
        palindrome = "".join(c.lower() for c in s if c.isalnum())
        reversed_palindrome = palindrome[::-1]

        for i in range(len(palindrome)):
            if palindrome[i] != reversed_palindrome[i]:
                is_palindrome = False
        return is_palindrome