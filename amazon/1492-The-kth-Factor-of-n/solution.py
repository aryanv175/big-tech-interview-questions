class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # i decided not to make a list to use less memory.
        # int k_th is where we store the k_th factor.
        for i in range(1, n+1):
            if n % i == 0: # if we find a factor, we put in k_th and we decrease k by 1
                k-= 1
                k_th = i
            if k == 0: #  when k is at 0, we have found the k_th factor and hence we return it
                return k_th
        return -1 # if we dont reach k==0 in the loop then that means that k> number of factors of n. So we return -1.
