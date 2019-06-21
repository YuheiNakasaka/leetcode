class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = ''
        b = bin(n)[2:].zfill(32)
        for i in range(len(b)):
            s = b[i] + s
        return int(s, 2)


solution = Solution()
print(solution.reverseBits(0b11111111111111111111111111111101))
print(solution.reverseBits(0b10111111111111111111111111111111))
print(solution.reverseBits(0b00000010100101000001111010011100))