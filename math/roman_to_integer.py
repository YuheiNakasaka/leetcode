# Input range is from 1 to 3999
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        prev = ""
        for char in s:
            total += roman[char]
            if prev != "" and roman[prev] < roman[char]:
                total -= roman[prev] + roman[char]
                total += roman[char] - roman[prev]
                prev = ""
            else:
              prev = char
        return total
        

solution = Solution()
print("Success") if solution.romanToInt("III") == 3 else print("Fail")
print("Success") if solution.romanToInt("IV") == 4 else print("Fail")
print("Success") if solution.romanToInt("IX") == 9 else print("Fail")
print("Success") if solution.romanToInt("XIV") == 14 else print("Fail")
print("Success") if solution.romanToInt("LVIII") == 58 else print("Fail")
print("Success") if solution.romanToInt("MCMXCIV") == 1994 else print("Fail")
print("Success") if solution.romanToInt("MMMCMXCIX") == 3999 else print("Fail")