class Solution:

    ROMAN_NUMS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:

        number = 0

        for i, char in enumerate(s):

            current = self.ROMAN_NUMS[char]

            next_value = 0
            if i + 1 < len(s):
                next_value = self.ROMAN_NUMS[s[i + 1]]

            if current < next_value:
                number -= current
            else:
                number += current

        return number
