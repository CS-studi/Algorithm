class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = dict()
        for item in strs:
            dkey = tuple(sorted(item))
            if dkey not in data:
                data[dkey] = []
            data[dkey].append(item)
        return data.values()