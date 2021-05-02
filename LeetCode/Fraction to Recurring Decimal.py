# Runtime: 32 ms, faster than 54.89% of Python3 online submissions for Fraction to Recurring Decimal.
# Memory Usage: 14.5 MB, less than 35.54% of Python3 online submissions for Fraction to Recurring Decimal.

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num = abs(numerator); denom = abs(denominator)
        q, non_cyc, cyc = self.check(num, denom)
        s = f'{q}.' + ''.join(map(str, non_cyc)) + '(' + ''.join(map(str, cyc)) + ')'
        if numerator < 0 and denominator > 0:
            s = str(numerator)[0] + s
        elif numerator > 0 and denominator < 0:
            s = str(denominator)[0] + s
        s = s.replace('(0)','')
        if s[-1] == '.':
            return s[:s.index('.')]
        return s

    def check(self, n, d):
        dividend = n;
        dividend_list = [];
        digit_list = []
        while True:
            if dividend in dividend_list:
                break
            dividend_list.append(dividend)
            digit = dividend // d
            dividend = (dividend % d) * 10
            digit_list.append(digit)
        idx = dividend_list.index(dividend)
        q = digit_list[0]
        non_cyc = digit_list[1:idx]
        cyc = digit_list[idx:]
        return q, non_cyc, cyc

if __name__ == '__main__':
    for a, b in [(1, 3), (1, 6), (1, 8), (4, 3), (15, 13), (2,1)]:
        print(f"{a}/{b} =", Solution().fractionToDecimal(b, a))




