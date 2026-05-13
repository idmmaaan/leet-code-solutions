class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = {}

        for str in strs:
            prefixes = []
            for i in range(len(str)):
                prefix = str[:i+1]
                prefixes.append(prefix)
                
            result[str] = prefixes

        sets_list = [set(val) for val in result.values()]
        common = set.intersection(*sets_list)

        if not common:
            return ''
        
        return max(common, key=len)
