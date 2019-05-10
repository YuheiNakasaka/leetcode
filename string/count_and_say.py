class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        term = "1"
        for i in range(n - 1):
            s = ""
            tmp = ""
            count = 0
            for char in term:
                if tmp == "" and tmp != char: 
                    tmp = char
                    count = 1
                elif tmp == char:
                    count += 1
                else:
                    s = s + str(count) + tmp
                    tmp = char
                    count = 1
            s = s + str(count) + tmp
            term = s
        return term

solution = Solution()
print("Success") if solution.countAndSay(1) == "1" else print("Fail")
print("Success") if solution.countAndSay(2) == "11" else print("Fail")
print("Success") if solution.countAndSay(3) == "21" else print("Fail")
print("Success") if solution.countAndSay(4) == "1211" else print("Fail")
print("Success") if solution.countAndSay(5) == "111221" else print("Fail")