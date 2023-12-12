from collections import Counter
def findSpecialInteger(self, arr: [int]) -> int:
        count = Counter(arr)
        for i in count.keys():
            if count[i] > len(arr) // 4:
                return i