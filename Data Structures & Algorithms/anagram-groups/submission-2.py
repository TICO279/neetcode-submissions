class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}

        for elem in strs:
            sort_elem = ''.join(sorted(elem))
            if sort_elem not in buckets.keys():
                buckets[sort_elem] = []
                buckets[sort_elem].append(elem)
            else:
                buckets[sort_elem].append(elem)
        
        return [value for value in buckets.values()]
