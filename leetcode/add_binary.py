def binary(a):
    return ord(a) - ord('0')

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = "0"
        i = len(a) - 1
        j = len(b) - 1
        if (i > j):
            b = "0" * (i-j) + b
        else:
            a = "0" * (j-i) + a
        k = len(a) - 1
        while(k >= 0):
            sum_at_pos_k = binary(a[k]) + binary(b[k]) + binary(carry)
            if sum_at_pos_k > 1:
                result_bit = str(sum_at_pos_k - 2)
                carry = str(sum_at_pos_k//2)
            else:
                result_bit = str(sum_at_pos_k)
                carry = "0"
            result = result_bit + result
            k -= 1
        if(binary(carry)):
            result = carry + result
        return result