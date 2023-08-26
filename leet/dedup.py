import math

def zigzig(s, numRows):
    if numRows == 1:
        return s
    res = ""
    for r in range(numRows):
        inc = 2 * (numRows - 1)
        for i in range(r, len(s), inc):
            res += s[i]
            if (0 < r < numRows - 1 and
                len(s) > i + inc - (2 * r)):
                res += s[i + inc - (2 * r)]
            print(res)
    return res



print("PAYPALISHIRING")
print("PINALSIGYAHRPI")
print(zigzig("PAYPALISHIRING", 4))
