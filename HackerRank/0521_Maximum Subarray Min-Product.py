from typing import List
class Solution:
    # Time Limit Exceeded
    def maxSumMinProduct(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                subarray = nums[i:j]
                max_val = max(min(subarray) * sum(subarray), max_val)
        return max_val

print(Solution().maxSumMinProduct([1,2,3,2]))
print(Solution().maxSumMinProduct([2,3,3,1,2]))
print(Solution().maxSumMinProduct([3,1,5,6,4,2]))
print(Solution().maxSumMinProduct(
    [80,88,117,53,134,124,90,122,25,113,185,179,
     116,82,18,77,12,182,30,6,88,166,28,174,43,190,
     63,133,45,142,41,85,144,110,119,60,104,162,48,
     48,164,169,111,102,8,189,158,51,116,152,110,100,
     2,181,55,53,72,193,181,17,148,27,138,48,94,84,51,
     118,30,68,172,126,136,164,81,153,100,157,101,151,
     30,90,91,118,159,45,173,181,77,158,152,22,173,35,
     81,31,62,79,30,47,96,178,37,131,100,108,153,36,148,
     99,109,48,125,163,138,178,166,45,143,43,126,74,36,
     48,81,116,159,14,92,3,125,35,50,99,144,130,168,127,
     105,176,126,107,182,114,126,43,22,145,8,195,57,75,
     9,71,58,138,74,44,200,118,145,191,198,197,127,141,
     131,29,147,30,69,199,140,94,139,194,11,195,185,113,
     140,56,109,27,189,168,193,64,77,9,116,68,90,23,113,
     31,199,61,54,189,151,177,90,182,157,162,110,43,158,
     36,53,53,16,146,90,137,72,153,138,44,83,181,75,75,
     147,69,132,174,25,35,193,106,16,71,168,33,180,34,64,
     38,183,83,64,195,174,101,126,37,148,162,69,161,107,
     97,116,20,163,197,24,104,132,192,72,178,95,117,125,
     84,149,1,199,188,24,188,118,163,171,179,92,17,137,102,
     56,110,55,127,69,83,73,87,141,148,34,145,125,88,175,
     196,13,12,26,161,118,5,32,41,113,117,1,110,52,177,34,
     167,78,41,71,24,168,93,65,22,96,171,167,43,14,102,161,
     79,186,180,194,60,110,168,24,181,25,1,55,123,20,34,152,
     58,133,175,114,3,3,179,88,31,109,178,34,123,19,59,99,
     23,188,27,27,81,95,77,36,98,199,193,35,165,174,37,18,
     136,145,3,157,167,43,113,90,185,55,161,192,39,106,158,
     176,114,56,23,26,36,193,32,151,187,99,90,110,81,36,64,
     71,166,22,64,142,154,154,185,156,73,200,177,7,169,78,53,
     133,156,131,49,192,101,76,166,14,62,127,99,29,62,128,164,
     153,19,136,4,93,82,34,100,146,108,94,140,175,45,196,121,
     198,19,5,151,18,4,68,56,11,16,102,130,74,161,183,129,197,
     107,109,180,103,22,164,138,138,158,40,72,22,80,21,131,53,
     40,138,84,101,151,163,196,167,175,165,17,80,179,112,187,
     62,15,63,23,112,30,117,157,156,15,80,171,190,169,190,45,
     31,4,182,36,180,3,42,128,89,134,133,185,67,43,96,33,192,
     200,69,188,31,198,8,86,110,70,135,17,68,183,148,161,20,
     128,117,131,93,15,128,146,43,95,41,66,198,27,147,173,186,
     30,59,190,131,1,12,4,63,12,121,94,99,39,46,10,142,183,190,
     168,108,58,83,64,107,185,82,70,20,147,96,31,129,173,14,46,58,133,12,103,18,120,73,199,80,84,23,142,117,3,95,52,75,145,78,190,160,63,119,95,152,127,198,199,51,188,140,195,63,39,2,105,7,60,139,89,163,178,3,86,1,195,169,97,189,187,79,27,53,136,61,108,126,16,37,183,72,24,12,60,134,106,180,96,118,192,22,149,25,130,35,164,101,20,152,146,16,112,170,34,61,75,67,81,101,180,189,84,82,116,70,60,20,52,35,200,198,150,28,40,28,43,116,120,81,105,31,138,92,198,54,116,79,119,68,31,24,41,176,78,181,179,155,11,56,84,38,24,183,64,92,102,132,13,174,77,67,45,8,104,116,143,192,141,64,25,119,27,36,32,4,16,200,57,34,51,103,96,176,162,166,22,150,151,67,20,6,17,51,166,114,33,24,85,32,11,119,13,44,147,111,186,102,128,8,98,175,110,45,91,55,48,71,72,115,39,9,158,159,158,63,166,76,128,106,141,123,16,23,72,99,36,108,52,165,135,64,162,140,5,98,183,92,123,140,125,89,145,129,83,100,70,47,7,82,153,57,8,200,72,15,121,136,92,197,150,60,41,26,64,169,62,69,137,189,15,196,57,148,100,91,45,46,61,152,82,189,179,92,152,8,181,180,91,146,145,37,145,49,127,139,80,45,126,10,24,15,60,155,57,6,135,123,1,85,158,52,34,88,184,46,83,16,6,38,151,181,37,199,29,135,94,19,96,181,170,102,151,26,87,78,83,35,41,188,112,164,125,167,82,45,182,144,178,158,92,58,171,151,45,97,79,188,177,76,33,46,187,1,180,147,101,198,146,9,47,155,82,157,57,164,145,27,128,37,85,191,20,61,89,82,43,163,23,182,172,164,187,86,115,3,68,54,64,178,18,90,66,28,185,1,13]))